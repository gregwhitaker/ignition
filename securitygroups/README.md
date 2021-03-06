# Security Groups
A security group acts as a virtual firewall that controls the traffic for one or more instances. When you launch an instance, you associate one or more security groups with the instance. You add rules to each security group that allow traffic to or from its associated instances. You can modify the rules for a security group at any time; the new rules are automatically applied to all instances that are associated with the security group.

## Setup Security Groups
Creates a default set of security groups.

    $ python securitygroups.py --setup --region REGION [--vpc-id VPC_ID] [--profile PROFILE]

## Teardown Security Groups
Removes the default set of security groups.

    $ python securitygroups.py --teardown --region REGION [--profile PROFILE]
