#! /bin/bash

source ../utils/environment.sh
source ../utils/cloudformation.sh
source ../utils/logging.sh
source ../utils/s3.sh

find_bucket_created_by_cloudformation nested-stacks-s3 NestedStackTemplatesBucket

delete_bucket $BUCKET

aws cloudformation delete-stack --stack-name "nested-stacks-s3" --region $REGION