---
company: "Raft"
title: "Senior DevSecOps Engineer / Platform Engineer"
period: "January 2024 - November 2025"
location: "Reston, VA"
order: 1
excerpt: "Platform engineering on production DoD ATO'd infrastructure, reducing build times 87% and expanding platform to support Java, C#, and PHP workloads."
---

## Scope

Platform engineering on production DoD ATO'd cloud infrastructure serving internal and tenant development teams. Led platform expansion, security posture improvement, and build performance optimization.

---

## Systems Influenced

**AWS Image Builder Pipeline**

- Migrated AMI builds from local Packer/Ansible execution to AWS Image Builder
- Integrated automated OSCAP security scanning and remediation
- **Impact:** Build time reduced from 40 minutes to 5 minutes (87.5% improvement)

**Container Build Tooling**

- Led migration from Kaniko to Buildah for rootless container builds
- Solved multi-stage and resource-intensive mono-repo build issues
- Maintained security posture while improving build reliability

**Platform Technology Stack Support**

- Expanded platform to support Java (Maven), C# .NET, and PHP
- Enabled broader tenant adoption across diverse technology stacks
- Increased platform value through multi-language workload support

**Security Scanning**

- Modernized dependency scanning with SBOM-based tooling
- Replaced legacy scanning methods
- Improved vulnerability detection accuracy

---

## Architectural Decisions

**Build Performance Architecture**

- Decision: Migrate from local tool execution to AWS Image Builder
- Rationale: Eliminate local tooling dependencies, integrate native AWS security scanning, reduce build time
- Outcome: 87.5% faster builds, automated security compliance

**Rootless Container Builds**

- Decision: Migrate to Buildah from Kaniko
- Rationale: Rootless execution, better multi-stage support, solve mono-repo resource constraints
- Outcome: Maintained security posture, improved build reliability

**Multi-Language Platform Support**

- Decision: Expand beyond initial language support to Java, C#, PHP
- Rationale: Enable broader tenant adoption, increase platform utility
- Outcome: Platform serves diverse workload types without custom infrastructure per language

---

## Measurable Outcomes

- **87.5% build time reduction** (40min → 5min for AMI builds)
- **3 new language stacks** enabled (Java, C#, PHP)
- **Automated security scanning** integrated into build pipelines
- **Tenant self-service** pipeline for external image approval
- **Zero security regressions** during tooling migrations

---

## Key Technologies

AWS Image Builder, Buildah, Kaniko, OSCAP, SBOM scanning, GitLab CI, Kubernetes, ALB, SES
