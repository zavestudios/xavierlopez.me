---
layout: single
title: "How to use Kubernetes secrets for Rails App configuration"
date: 2022-06-30 14:21:46 -0800
categories: configuration containerization software-development virtualization
---

For Rails apps that I deploy to a Kubernetes cluster, I like to push as much environment configuration as I can to Kubernetes secrets.  Here's what my app-config-secret yml looks like:

apiVersion: v1
kind: Secret
metadata:
  name: app-name
  namespace: app-namespace-name
data:
  db_host: base64-encoded-value
  db_name: base64-encoded-value
  db_username: base64-encoded-value
  db_password: base64-encoded-value
  db_port: base64-encoded-value
  secret_key_base: base64-encoded-value
  rails_serve_static_files: base64-encoded-value

I like to put the secret_key_base and rails_serve_static_files keys in this secret, in addition to the db connection keys, but let's ignore those for the purposes of this post.  

The thing is, you have to [base 64](https://linux.die.net/man/1/base64) encode these values before you stuff them in this secret. Let's do that with a boolean string and test it out by decoding it:

ᐅ echo 'true' | base64
dHJ1ZQ==
ᐅ echo 'dHJ1ZQ==' |base64 -D
true

Now do that to all the values you want to put in the Secret manifest file above, then run:

`kubectl apply -f /path/to/the/secrets/file.yml` 

That will turn those values into environment variables, that can be accessed by your application. First, edit your database.yml to look like this:

your_environment:
  <<: *default
  host: <%= ENV['DB_HOST'] %>
  database: <%= ENV['DB_NAME'] %>
  username: <%= ENV['DB_USER_NAME'] %>
  password: <%= ENV['DB_PASSWORD'] %>
  port: <%= ENV['DB_PORT'] %>

Then edit your application deployment yml to access the environment variables from the secret, thusly:

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: app-name
  name: app-name
  namespace: app-namespace-name
spec:
  replicas: 3
  revisionHistoryLimit: 2
selector:
  matchLabels:
    app: app-name
template:
  metadata:
    labels:
      app: app-name
  spec:
    imagePullSecrets:
    - name: the-docker-hub-secret (a different conversation)
    containers:
    - name: app-name
      image: your-repo/image-name:tag
      command: ["/bin/sh", "-c","rake db:migrate && rake db:seed && rails server --port 3000 --binding 0.0.0.0"]
      env:
      - name: DB_HOST
        valueFrom:
          secretKeyRef:
            name: app-name-secrets (whatever you named it)
            key: db_host
      - name: DB_NAME
        valueFrom:
          secretKeyRef:
            name: app-name-secrets (whatever you named it)
            key: db_name
      - name: DB_USER_NAME
        valueFrom:
          secretKeyRef:
            name: app-name-secrets (whatever you named it)
            key: db_username
      - name: DB_PASSWORD
        valueFrom:
          secretKeyRef:
            name: app-name-secrets (whatever you named it)
            key: db_password
      - name: DB_PORT
        valueFrom:
          secretKeyRef:
            name: app-name-secrets (whatever you named it)
            key: db_port
      - name: SECRET_KEY_BASE
        valueFrom:
          secretKeyRef:
            name: app-name-secrets (whatever you named it)
            key: secret_key_base
      - name: RAILS_SERVE_STATIC_FILES
        valueFrom:
          secretKeyRef:
            name: app-name-secrets (whatever you named it)
            key: rails_serve_static_files

That'll do it.