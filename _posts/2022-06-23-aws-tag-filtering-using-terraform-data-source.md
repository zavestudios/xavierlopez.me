---
layout: single
title: "AWS tag filtering using Terraform data source"
date: 2022-06-23 11:04:42 -0800
categories: networking software-development tools virtualization
---

This is how you filter an AWS resource by tag. I needed to do this in order to add a route through a vpc peering connection for each route table. I wanted the code to be DRY, and I wanted it to work even though I would not know the route table ids until run time. So here's what I did:

```hcl
data "aws_route_tables" "my_rts" {
  # I'm using the terraform vpc module
  vpc_id = module.vpc.vpc_id

  filter {
    name   = "tag:Name"
    values = ["my-route-table-private", "my-route-table-public"]
  }
}

resource "aws_route" "my_routes" {
  for_each                  = toset(data.aws_route_tables.my_rts.ids)
  route_table_id            = each.value
  destination_cidr_block    = "<your_cidr_block>"
  vpc_peering_connection_id = aws_vpc_peering_connection.my_px.id
}
```

I started this off by using the data source of the aws route tables Terraform resource, then filtered them by tag. Then I created a route for each table that hits the peering connection when trying to go to the other vpc. If you look at the documentation, you'll notice that they use the count meta-argument. I was having trouble doing it the way they did it, so I went with `toset()` and `for_each`.