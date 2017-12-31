CloudFormation
===
AWS CloudFormation gives developers and systems administrators an easy way to create and manage a collection of related AWS resources, provisioning and updating them in an orderly and predictable fashion.  

You can deploy and update a template and its associated collection of resources (called a stack) by using the AWS Management Console, AWS Command Line Interface, or APIs.

The IAM scripts can be used to configure the following:
* S3 Bucket for Nested Stacks (Reusable CloudFormation Templates)

## Setup Nested Stacks
Creates an S3 bucket to hold CloudFormation nested stacks.

    $ python nested-stacks.py --setup --bucket BUCKET

## Teardown Nested Stacks
Deletes the S3 bucket that holds the CloudFormation nested stacks.

    $ python nested-stacks.py --teardown --bucket BUCKET
