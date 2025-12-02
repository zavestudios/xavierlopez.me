---
layout: page
title: Xavier G. Lopez
---

**Senior Platform Engineer | Sec+ | TS/SCI | DoD 8570 IAT II certified**

[xavier@xavierlopez.me](mailto:xavier@xavierlopez.me) • (951) 456-2190 • [linkedin.com/in/zavelopez](https://linkedin.com/in/zavelopez)

---

## Professional Summary

Creates leverage for the business by developing and operating platforms composed of carefully chosen OSS, COTS, and cloud services, drawing from a decade of experience in DevOps, site reliability engineering, cloud architecture and Agile application development. Reinforces internal and tenant developer productivity by insulating them from operational complexity – providing platform usage telemetry, handling service dependencies, executing software migrations – thereby freeing them to innovate at the application layer.

---

## Technical Expertise

- **CI/CD:** Pipelines for tenant self-service, delivery, continuous integration and IaC provisioning
- **AWS Architecture:** Load balancing, image management, RBAC, EC2 auto scaling, identity and access management, managed RDBMS, DNS, object storage, file systems, compute, networking, threat detection
- **Kubernetes:** Base image hardening, multi-tenancy, network policies, monitoring with metrics, storage, service meshing, logging, Helm
- **Infrastructure as Code:** Terraform
- **Application Support:** Java, Node, .NET, PHP, Python
- **Monitoring & Observability:** Grafana, Prometheus
- **Programming and Scripting:** Ansible, Bash, Python, Ruby on Rails, YAML
- **Security & Compliance:** Cloud, container, dependency scanning, static app testing, dynamic app testing, Terraform scanning, vulnerability management
- **GitOps:** ArgoCD, FluxCD

---

## Professional Experience

### Senior DevSecOps Engineer / Platform Engineer
**Raft, Reston, VA** | *January 2024 - November 2024*

Led, paired and mentored on platform engineering stories and tenant tickets on production DoD ATO'd cloud infrastructure serving internal and tenant development teams. Architected and implemented scalable solutions reducing build times 87% while enhancing security posture.

- Migrated the Amazon Machine Image (AMI) build process from local execution of Packer/Ansible to AWS Image Builder, reducing build time from 40 minutes to 5 minutes (87.5% improvement, as measured by tech lead) while integrating automated OSCAP security scanning and remediation
- Led image-build tooling migration to Buildah from Kaniko, implementing rootless container builds, maintaining security posture while solving issues involving multi-stage and resource intensive mono-repo builds
- Led expansion of the platform by adding support for Java (Maven), C# .NET, and PHP technology stacks, enabling broader tenant team adoption and increasing platform value
- Modernized security tooling by implementing SBOM-based dependency scanning, replacing legacy scanning methods and improving vulnerability detection accuracy
- Built tenant self-service pipeline for requesting external image approval
- Configured complex infrastructure components including ALB listener rules, GitLab Workspace network policies, and SES integration across multiple applications
- Encapsulated the Gitlab API to enhance cross-team collaboration for vulnerability management and reduce load on the help-desk
- Piloted token authentication for dynamic application security testing in testing stage of CI pipeline

### DevOps Engineer / SRE
**Saasoft, Fillmore, CA** | *May 2023 - January 2024*

- Maintained GitOps-driven CI/CD pipelines with version-controlled infrastructure and application code for efficient software delivery
- Implemented Prometheus instrumentation for web applications, improving observability and enabling data-driven optimizations
- Developed Ruby on Rails features including REST APIs, microservices architecture, and authentication/authorization

### DevOps Engineer / SRE - Platform Lead
**Insight Direct, Chandler, AZ** | *July 2018 - May 2023*

Led platform transformation from bare metal infrastructure to hybrid architecture. Successfully managed staging, QA and production EKS clusters.

- Architected and executed migration from bare metal/VM deployments to automated CI/CD pipelines deploying to Kubernetes (EKS and on-premises), providing the organization with its first cloud infrastructure
- Scaled Kubernetes infrastructure across multiple clusters and environments
- Deployed enterprise monitoring stack (Prometheus, Grafana, AlertManager) providing the team's first observability solution
- Increased release frequency through GitLab CI/CD merge request pipelines
- Enhanced EKS cluster security through closer adherence to the AWS Well-Architected Framework, implementing the organization's first shift-left initiative
- Reduced application deployment time from 30+ minutes to under 5 minutes by packaging Kubernetes manifests and pipeline optimization
- Lowered operational costs 25% through strategic cloud migration of data workloads and right-sizing infrastructure resources

### Full Stack Developer / DevOps Consultant
**Juniper Networks, Sunnyvale, CA** | *July 2016 - July 2018*

Led and paired on network device automation projects.

- Consulted enterprise customers on network device API automation, reducing manual errors and improving operational efficiency
- Developed automation tooling for network configuration management enabling non-technical staff to perform security-critical tasks
- Designed POC for orchestrating live network device software/firmware updates with zero downtime

### Full Stack Developer / DevOps Engineer
**Datalink, Eden Prairie, MN** | *November 2013 - June 2016*

Led the application development team's adoption of DevOps.

- Developed and deployed .NET/C# and Ruby on Rails web application stacks
- Designed deployment automation code for .NET and Ruby on Rails applications, streamlining release processes and preparing the team for continuous integration
- Led Linux web server configuration management adoption with Chef, standardizing infrastructure and reducing configuration drift
- Led the company's adoption of Heroku

---

## Education

**Bachelor of Arts**
California State University, San Bernardino, CA

---

## Certifications & Clearances

- Security+ Certification (Active)
- TS/SCI Security Clearance (Active)
