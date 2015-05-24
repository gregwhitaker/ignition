CloudTrail
===

CloudTrail provides a record of your AWS API calls.  You can use this data to gain visibility into user activity, troubleshoot operational and security incidents, or to help demonstrate compliance with internal policies or regulatory standards.

##setup-cloudtrail.sh
Enables CloudTrail monitoring and creates an S3 bucket to store CloudTrail logs.

    ./setup-cloudtrail.sh <bucket> [bucket_prefix]

##teardown-cloudtrail.sh
Disables CloudTrail monitoring and removes the S3 bucket used to store CloudTrail logs.

    ./teardown-cloudtrail.sh
