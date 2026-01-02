---
layout: single
title: "Key and Certificate Extraction from a .pfx file"
date: 2022-03-24 09:13:51 -0800
categories: system-administration
---

Sometimes you ask someone in your IT department for an SSL certificate to use in a project you have running somewhere on the internet.  He obliges.  You feel puffed up with pride, because you've always considered SSL, and everything associated with it, to be heady stuff.  Then you look at what he sent you.

The only thing you're sure of, at this point, is that you need to untar the contents.  Ok, that's better than being stuck, but after seeing the resulting files you wonder if you should call the sender back and ask him what you're supposed to do with all this stuff.  You don't want to do that though, because he might tell you to RTFM.

That's never happened to you?  Oh. 

Well, for those of us who've faced this crucible, here's what we're going to do. First off, we should know that the .pfx (PKCS#12) file format is for safely packaging the public key, which is the certificate, and a private key. Our objective is to extract those two units for use on another server. We're going to use openssl to accomplish this.

Read the password from the txt file that was included in the zip file that was sent to you. You'll need it later:

```bash
cat password.txt
```

Extract the private key. You'll be prompted for the password:

```bash
openssl pkcs12 -in [yourfile.pfx] -nocerts -out [your.key]
```

Extract the certificate:

```bash
openssl pkcs12 -in [yourfile.pfx] -clcerts -nokeys -out [your.crt]
```

Decrypt the private key. You'll be prompted again for the password:

```bash
openssl rsa -in [your.key] -out [your-decrypted.key]
```