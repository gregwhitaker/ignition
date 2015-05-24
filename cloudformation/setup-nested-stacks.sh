#! /bin/bash

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

aws cloudformation create-stack --stack-name nested-stacks-s3 --template-body file://./templates/nested-stacks-s3.json --region $REGION --parameters ParameterKey=S3BucketName,ParameterValue=$1
wait_for_stack "nested-stacks-s3"