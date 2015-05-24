#! /bin/bash

source ../utils/environment.sh
source ../utils/cloudformation.sh
source ../utils/logging.sh
source ../utils/s3.sh

aws cloudformation delete-stack --stack-name "nested-stacks-s3" --region $REGION