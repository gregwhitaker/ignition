#! /bin/bash

#/ Usage: setup-user-group
#/ Creates a group with full access privileges, excluding IAM management.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

# Creating Role
aws cloudformation create-stack --stack-name "iam-user-group" --template-body file://./templates/iam-user-group.json --region $REGION --capabilities CAPABILITY_IAM
wait_for_stack "iam-user-group"