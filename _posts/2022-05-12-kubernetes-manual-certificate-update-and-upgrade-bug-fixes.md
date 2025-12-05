---
layout: single
title: "Kubernetes Manual Certificate Update and Upgrade-bug Fixes"
date: 2022-05-12 14:57:55 -0800
categories: virtualization
---

About one year ago, I set up an on-premises Kubernetes cluster. Keeping track of the SSL certs slipped my mind, and I woke up one morning to an inaccessible cluster. Embarrassingly, I'd also failed to update the 3 CentOS servers that make up the cluster.  For a whole year.  Twelve hundred package updates later and ... I had an out-of-date-certificates problem, and a few new Kubernetes configuration bugs to deal with.

No biggie. Let's fix it -- people are depending on us. 

This post assumes you've used kubeadm to set up your cluster. First, let's become root and confirm that our certificates are expired:

`sudo su -` 

`kubeadm alpha certs check-expiration`

Now let's renew those expired certificates:

`kubeadm alpha certs renew all` 

That will take care of the certificates, which leaves us with the bugs.  The package updates left me with a newer version of kubernetes.  There are some changes in the way that we configure parts of the cluster, in version 1.18. I found it necessary to edit flanneld:

`kubectl edit cm -n kube-system kube-flannel-cfg`

Add this part:

```
{
  "name": "cbr0",
  "cniVersion": "0.3.1",  <<<<<<<<<<<<<<<<
  "plugins": [
    {
      "type": "flannel",
      "delegate": {
        "hairpinMode": true,
        "isDefaultGateway": true
      }
    },
    {
      "type": "portmap",
      "capabilities": {
      "portMappings": true
      }
    }
  ]
}
```

The next issue requires us to edit /var/lib/kubelet/config.yml. Just add this to the end of the file, but if you're the organized type, put it in the proper place, alphabetically:

`featureGates:
CSIMigration: false`

This is just a few of the issues that I've encountered lately with my cluster. I'll add more to this post, as I begin dealing with them.