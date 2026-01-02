---
layout: single
title: "Authenticating Gitlab-Runner to Kubernetes"
date: 2022-11-04 15:56:02 -0800
categories: configuration containerization software-development
---

## Gitlab-Runner Can't Talk to the K8s API

This is a post about how we authenticated our gitlab-runner to an on-premises kubernetes cluster. It was a nasty problem to deal with and I suspect it'll need to be done again in the future, so I thought I'd document it here, in order not to have to start from scratch. 

I think it all started when we moved our Gitlab instance to the "DMZ", but I'm not certain. First, the gitlab-runner would be greyed out in the [Gitlab CI/CD Settings](https://docs.gitlab.com/ee/ci/quick_start/#configuring-a-runner).  I was able to get it running again a couple of times, then on the third occurrence of the problem, I decided to delete the runner and start fresh with a new one. I wish I had that decision to do over, because I would have backed up a few items first. 

In any case, after creating a new runner and successfully registering it with the Gitlab server, we started to see this error in the running job output:

## Gitlab + Gitlab Runner + On Premises Kubernetes

```
Running with gitlab-runner 12.9.0 (4c96e5ad)
on on-prem-staging xxxxxx
Preparing the "kubernetes" executor
00:00
WARNING: Namespace is empty, therefore assuming 'default'.
Using Kubernetes namespace: default
Using Kubernetes executor with image docker:latest …
Preparing environment
00:00
Uploading artifacts for failed job
00:01
ERROR: Job failed (system failure): Get https://xx.xx.xx.xx:6443/version?timeout=32s: x509: certificate signed by unknown authority
```

As you can see, we use the gitlab-runner, with the kubernetes executor. It's called upon by our Gitlab instance, and connects to our on-premises kubernetes cluster to create deployment resources. Those are 3 distinct entities: gitlab-runner on its own host, the gitlab server on its own host, and the kubernetes cluster control plane on a different host. Capisce?  To reiterate, this kubernetes cluster does not reside on a cloud provider. It is in our network. 

Admittedly, running the gitlab-runner on a separate host is a bit more complexity than is desirable. In the near future, we will be putting it inside of the cluster, as opposed to running it from its own host. It will be simpler that way. 

## Configuring Gitlab-Runner

So here's what we learned. All communication with the kubernetes cluster is via the [kubernetes rest api](https://v1-17.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.17/). The communication model is client-server, so everyone who wants to communicate with the cluster is a client. [Kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) is a client. [Lens ](https://k8slens.dev/)is a client. The gitlab-runner is a client. As such, it must be configured to authenticate.

The gitlab-runner is configured using a file on the host where it runs. That file is found at: /etc/gitlab-runner/config.toml. Here's an example:

```toml
concurrent = 4
log_level = "warning"
[session_server]
  listen_address = "[::]:8093" # listen on all available interfaces on port 8093
  advertise_address = "runner-host-name.tld:8093"
  session_timeout = 1800
[[runners]]
  name = "ruby-2.6-docker"
  url = "https://CI/"
  token = "TOKEN"
  limit = 0
  executor = "docker"
  builds_dir = ""
  shell = ""
  environment = ["ENV=value", "LC_ALL=en_US.UTF-8"]
  clone_url = "http://gitlab.example.local"
[runners.kubernetes]
  host = "https://45.67.34.123:4892"
  cert_file = "/etc/ssl/kubernetes/api.crt"
  key_file = "/etc/ssl/kubernetes/api.key"
  ca_file = "/etc/ssl/kubernetes/ca.crt"
  image = "golang:1.8"
  privileged = true
  allow_privilege_escalation = true
  image_pull_secrets = ["docker-registry-credentials"]
```

## The Core of the Problem

The part that was killing us was the cert_file, key_file, and ca_file. So here's what we did. We went to the control plane of the kubernetes cluster (master) and copied `/etc/kubernetes/pki/ca.crt` & `/etc/kubernetes/pki/ca.key` to our workstation. Those are certificates that we updated a while back, in this [post](https://xavierlopez.me/virtualization/kubernetes-manual-certificate-update-and-upgrade-bug-fixes/). Once we had it safely in our sandbox, we generated a certificate signing request:

```bash
openssl req -newkey rsa:2048 -nodes -keyout gitlab-admin.key -out gitlab-admin.csr -subj "/CN=gitlab-admin"
```

We used the name gitlab-admin because that is the name of the service account in the cluster that runs the job. Then we signed the certificate signing request using the files we copied from the control plane:

```bash
openssl x509 -req -in gitlab-admin.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out gitlab-admin.crt -days 1000
```

Then we copied the artifacts from those two commands (`gitlab-admin.crt`, `gitlab-admin.key`, and `ca.crt`) to `/etc/ssl/kubernetes/` on the gitlab-runner host, and added them to `/etc/gitlab-runner/config.toml`. The way you see it above.

## Almost There. Just Two More Steps

There were two more important steps. The gitlab-admin user in the cluster did not have permission to do everything we needed it to do in the kubernetes api, so we gave it the cluster-admin role, like this:

```bash
kubectl create clusterrolebinding gitlab-admin --clusterrole=cluster-admin --user=gitlab-admin
```

That solved that problem for user gitlab-admin in the build stage, but unexpectedly, the deploy stage used a different user. This one named 'system:serviceaccount:default:default'. Why? I do not know. We'll have to research that later on. In order for that user to authenticate with the kubernetes api to do its work, we chose method #1 of [this tutorial](https://medium.com/@shalkam/how-to-update-kubernetes-deployment-image-using-gitlab-ci-yml-1c3faa4899e4). Later, we'll switch to method #2. Thanks for reading!