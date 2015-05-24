CloudFormation
===
AWS CloudFormation gives developers and systems administrators an easy way to create and manage a collection of related AWS resources, provisioning and updating them in an orderly and predictable fashion.  

You can deploy and update a template and its associated collection of resources (called a stack) by using the AWS Management Console, AWS Command Line Interface, or APIs.

##setup-nested-stacks
Creates an S3 bucket to hold CloudFormation nested stacks.

    ./setup-nested-stacks <bucket name>

##teardown-nested-stacks
Deletes the S3 bucket that holds the CloudFormation nested stacks.

    ./teardown-nested-stacks <bucket name>
