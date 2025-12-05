---
layout: single
title: "Kubernetes Cluster Configuration"
date: 2023-08-15 15:58:13 -0800
categories: configuration kubernetes
---

I was in the process of installing [Prometheus](https://prometheus.io/docs/introduction/overview/) and needed to have a couple of features enabled in an on-premises cluster, but didn't know where to get and set that information.  My research uncovered these handy little command lines for viewing two of the most important configurations in your cluster. The first is for the [kubelet](https://kubernetes.io/docs/concepts/overview/components/#kubelet).  The kubelet-config is one the sources from which the kubelet reads its configuration.  

```
kubectl describe cm kubeadm-config -n kube-system 

Name: kubelet-config
Namespace: kube-system
Labels:
Annotations:

Data

kubelet:

apiVersion: kubelet.config.k8s.io/v1beta1
authentication:
anonymous:
enabled: false
webhook:
cacheTTL: 0s
enabled: true
x509:
clientCAFile: /var/lib/minikube/certs/ca.crt
authorization:
mode: Webhook
webhook:
cacheAuthorizedTTL: 0s
cacheUnauthorizedTTL: 0s
cgroupDriver: systemd
clusterDNS:
- 10.96.0.10
clusterDomain: cluster.local
containerRuntimeEndpoint: ""
cpuManagerReconcilePeriod: 0s
evictionHard:
imagefs.available: 0%
nodefs.available: 0%
nodefs.inodesFree: 0%
evictionPressureTransitionPeriod: 0s
failSwapOn: false
fileCheckFrequency: 0s
hairpinMode: hairpin-veth
healthzBindAddress: 127.0.0.1
healthzPort: 10248
httpCheckFrequency: 0s
imageGCHighThresholdPercent: 100
imageMinimumGCAge: 0s
kind: KubeletConfiguration
logging:
flushFrequency: 0
options:
json:
infoBufferSize: "0"
verbosity: 0
memorySwap: {}
nodeStatusReportFrequency: 0s
nodeStatusUpdateFrequency: 0s
rotateCertificates: true
runtimeRequestTimeout: 15m0s
shutdownGracePeriod: 0s
shutdownGracePeriodCriticalPods: 0s
staticPodPath: /etc/kubernetes/manifests
streamingConnectionIdleTimeout: 0s
syncFrequency: 0s
volumeStatsAggPeriod: 0s

BinaryData
====
Events: <none>
```

That's the output from my [Minikube](https://minikube.sigs.k8s.io/docs/). As you can see, it's verbose. Have fun configuring.

If you used [kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) to provision your cluster, then you can use  this next example to read  the ConfigMap for kubeadm:

```
kubectl describe cm kubeadm-config -n kube-system
Name:         kubeadm-config
Namespace:    kube-system
Labels:       <none>
Annotations:  <none>

Data
====
ClusterConfiguration:
----
apiServer:
  certSANs:
  - 127.0.0.1
  - localhost
  - 192.168.49.2
  extraArgs:
    authorization-mode: Node,RBAC
    enable-admission-plugins: NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,DefaultTolerationSeconds,NodeRestriction,MutatingAdmissionWebhook,ValidatingAdmissionWebhook,ResourceQuota
  timeoutForControlPlane: 4m0s
apiVersion: kubeadm.k8s.io/v1beta3
certificatesDir: /var/lib/minikube/certs
clusterName: mk
controlPlaneEndpoint: control-plane.minikube.internal:8443
controllerManager:
  extraArgs:
    allocate-node-cidrs: "true"
    leader-elect: "false"
dns: {}
etcd:
  local:
    dataDir: /var/lib/minikube/etcd
    extraArgs:
      proxy-refresh-interval: "70000"
imageRepository: registry.k8s.io
kind: ClusterConfiguration
kubernetesVersion: v1.27.3
networking:
  dnsDomain: cluster.local
  podSubnet: 10.244.0.0/16
  serviceSubnet: 10.96.0.0/12
scheduler:
  extraArgs:
    leader-elect: "false"

BinaryData
====

Events:  <none>
```

These are exceedingly important ConfigMaps to be familiar with, as they are fundamental to your cluster, so it's a good idea to have these command lines quickly available. Thanks for reading!