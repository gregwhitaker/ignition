#! /bin/bash

#/ Usage: setup-nested-stacks <bucket>
#/ Creates an S3 bucket to hold CloudFormation nested stack templates.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

usage() {
	echo "Usage: setup-nested-stacks <bucket>"
}

if [ -z "$1" ]; then
	echo "S3 bucket name is required!"
	usage
	exit 1
fi

aws cloudformation create-stack --stack-name nested-stacks-s3 --template-body file://./templates/nested-stacks-s3.json --region $REGION --parameters ParameterKey=S3BucketName,ParameterValue=$1
wait_for_stack "nested-stacks-s3"