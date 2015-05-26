#! /bin/bash

#/ Usage: setup-detailed-billing <bucket>
#/ Creates an S3 bucket to hold detailed billing reports.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

usage() {
	echo "Usage: setup-detailed-billing <bucket>"
}

if [ -z "$1" ]; then
	echo "S3 bucket name is required!"
	usage
	exit 1
fi

# Creating S3 Bucket
aws cloudformation create-stack --stack-name "detailed-billing-s3" --template-body file://./templates/detailed-billing-s3.json --region $REGION --parameters ParameterKey=S3BucketName,ParameterValue=$1
wait_for_stack "detailed-billing-s3"