#! /bin/bash

#/ Usage: setup-config
#/ Enables Config and creates an S3 Bucket and SNS Topic to receive configuration events.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

usage() {
	echo "Usage: setup-config"
}

# Creating S3 Bucket
aws --output text cloudformation create-stack --stack-name "config-s3" --template-body file://./templates/config-s3.json --region $REGION --parameters ParameterKey=S3BucketName,ParameterValue=$1
wait_for_stack "config-s3"

find_arn_created_by_cloudformation "config-s3" "ConfigBucket"
BUCKET_ARN=$CF_ARN

# Creating SNS Topic
aws --output text cloudformation create-stack --stack-name "config-sns" --template-body file://./templates/config-sns.json --region $REGION --parameters ParameterKey=S3BucketName,ParameterValue=$1
wait_for_stack "config-sns"

find_arn_created_by_cloudformation "config-sns" "ConfigTopic"
TOPIC_ARN=$CF_ARN

# TODO Add Delivery Channels

# TODO Start the Configuration Recorder