---
layout: single
title: "Kubernetes Cheatsheet"
date: 2022-03-11 14:42:52 -0800
categories: software-development system-administration virtualization
---

You know how we do it.  We do a hundred things a day, but we don't try to memorize it all.  For this, we have cheatsheets. Here's another one.

See everything in your cluster, all at once, in the default namespace:

```bash
kubectl get all
```

See everything in every namespace:

```bash
kubectl get all --all-namespaces
```

Shell into a running pod container:

```bash
kubectl exec -it <name-of-pod> sh
```

Get the logs for a pod container:

```bash
kubectl logs <name-of-pod>
```

Create a secret for Docker registry authentication:

```bash
kubectl create secret docker-registry mydockerhubsecret \
  --docker-username=myusername --docker-password=mypassword \
  --docker-email=my.email@provider.com
```

Copy a secret from one namespace to another:

```bash
kubectl get secret <secret-name> --namespace=<source-namespace> --export -o yaml | \
  kubectl apply --namespace=destination-namespace -f -
```

Check the logs of your nginx ingress controller. This is a jackpot of useful information:

```bash
kubectl logs -n ingress-nginx <ingress-nginx-controller-pod-name>
```

Check the nginx configuration of a controller pod:

```bash
kubectl exec -it -n ingress-nginx nginx-ingress-controller-name cat /etc/nginx/nginx.conf
```

More to come.