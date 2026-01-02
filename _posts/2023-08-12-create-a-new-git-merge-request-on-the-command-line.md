---
layout: single
title: "Create a New Git Merge Request on the Command Line"
date: 2023-08-12 12:04:47 -0800
categories: software-development tools
---

Let's create a merge request from the command line. You can do this in the Gitlab UI, but why change contexts? As a developer, you're familiar with the workflow. You just finished making some code edits. You've run them on your workstation and they look good to you. Now you want to send them off for review. I've configured a job to create a [Review App](https://docs.gitlab.com/ee/ci/review_apps/) as the first step in our [Merge Request pipelines](https://docs.gitlab.com/ee/ci/pipelines/merge_request_pipelines.html). So this push will trigger that to happen. If the Scrum Product Owner is satisfied with your work after seeing the Review App, they will approve the merge, which will delete the Review App and trigger the job to build and deploy that commit to the target branch. The 'main' branch, in this case.

```bash
git add --all

git commit -am "Git commit message"

git push -o merge_request.create \
  -o merge_request.assign="product-owner@your-company.com" \
  -o merge_request.description="Finished story number 123" \
  -o merge_request.target=main
```