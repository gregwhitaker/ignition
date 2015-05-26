#! /bin/bash

#/ Usage: teardown-detailed-billing <bucket>
#/ Deletes the S3 bucket that holds detailed billing reports.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

usage() {
	echo "Usage: teardown-detailed-billing <bucket>"
}

if [ -z "$1" ]; then
	echo "S3 bucket name is required!"
	usage
	exit 1
fi

# Delete the nested stack templates bucket
find_resource_created_by_cloudformation "detailed-billing-s3" "BillingReportsBucket"
delete_bucket $CF_RESX

# Delete the CloudFormation stack that created the detailed billing reports S3 bucket
aws cloudformation delete-stack --stack-name "detailed-billing-s3" --region $REGION