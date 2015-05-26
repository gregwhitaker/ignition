#! /bin/bash

#/ Usage: setup-config
#/ Enables Config and creates an S3 Bucket and SNS Topic to receive configuration events.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

usage() {
	echo "Usage: setup-config [bucket] [topic]"
}

# Defaulting S3 bucket name if not provided
unset BUCKET
if [ -z $1 ]; then
	if [[ -n "$ACCT_NUM" ]]; then
		BUCKET="config-$ACCT_NUM"
	else
		BUCKET="config"
	fi

	echo "$(tput setaf 2)Defaulting Config Bucket Name to '$(tput setaf 3)$BUCKET$(tput setaf 2)'$(tput sgr0)"
else
	BUCKET="$1"
fi

# Defaulting topic name if not provided
unset TOPIC
if [ -z $2 ]; then
	if [[ -n "$ACCT_NUM" ]]; then
		TOPIC="config-$ACCT_NUM"
	else
		TOPIC="config"
	fi

	echo "$(tput setaf 2)Defaulting Config Topic Name to '$(tput setaf 3)$TOPIC$(tput setaf 2)'$(tput sgr0)"
else
	TOPIC="$2"
fi

# Creating S3 Bucket
aws --output text cloudformation create-stack --stack-name "config-s3" \
	--template-body file://./templates/config-s3.json \
	--region "$REGION" \
	--parameters "ParameterKey=S3BucketName,ParameterValue=$BUCKET"

wait_for_stack "config-s3"

# Looking up the ARN of the S3 Bucket
find_arn_created_by_cloudformation "config-s3" "ConfigBucket"
BUCKET_ARN=$CF_ARN

echo "$(tput setaf 2)Created Bucket '$(tput setaf 3)$BUCKET_ARN$(tput setaf 2)'$(tput sgr0)"

# Creating SNS Topic
aws --output text cloudformation create-stack --stack-name "config-sns" \
	--template-body file://./templates/config-sns.json \
	--region "$REGION" \
	--parameters "ParameterKey=SNSTopicName,ParameterValue=$TOPIC"

wait_for_stack "config-sns"

# Looking up the ARN of the SNS Topic
find_arn_created_by_cloudformation "config-sns" "ConfigTopic"
TOPIC_ARN=$CF_ARN

echo "$(tput setaf 2)Created Topic '$(tput setaf 3)$TOPIC_ARN$(tput setaf 2)'$(tput sgr0)"

# TODO Add Delivery Channels

# TODO Start the Configuration Recorder