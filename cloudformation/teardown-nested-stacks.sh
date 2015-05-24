#! /bin/bash

#/ Usage: teardown-nested-stacks <bucket>
#/ Deletes the S3 bucket that stores CloudFormation nested stack templates.

source ../utils/environment.sh
source ../utils/cloudformation.sh
source ../utils/logging.sh
source ../utils/s3.sh

# Delete the nested stack templates bucket
find_bucket_created_by_cloudformation nested-stacks-s3 NestedStackTemplatesBucket
delete_bucket $BUCKET

# Delete the CloudFormation stack that created the CloudFormation nested stack templates S3 bucket
aws cloudformation delete-stack --stack-name "nested-stacks-s3" --region $REGION