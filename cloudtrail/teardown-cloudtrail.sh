#! /bin/bash

#/ Usage: teardown_cloudtrail <bucket>
#/ Deletes the CloudTrail bucket, disables CloudTrail and deletes all CloudFormation templates used to enable CloudTrail.

source ../utils/environment.sh
source ../utils/cloudformation.sh
source ../utils/logging.sh
source ../utils/s3.sh

# Flush the CloudTrail bucket of data
BUCKET=find_bucket_created_by_cloudformation $1 CloudTrailBucket
flush_bucket $BUCKET

# Delete the CloudFormation stack that enabled CloudTrail
aws cloudformation delete-stack --stack-name cloudtrail --region $REGION
wait_for_stack cloudtrail

# Delete the CloudFormation stack that configured the S3 bucket policy for CloudTrail
aws cloudformation delete-stack --stack-name cloudtrail-s3-policy --region $REGION
wait_for_stack cloudtrail-s3-policy

# Delete the CloudFormation stack that created the CloudTrail S3 bucket
aws cloudformation delete-stack --stack-name cloudtrail-s3 --region $REGION
wait_for_stack cloudtrail-s3 