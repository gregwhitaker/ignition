#! /bin/bash

#/ Usage: setup-user-role
#/ Creates a role with full access privileges, excluding IAM management.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

# Creating Role
aws cloudformation create-stack --stack-name "iam-user-role" --template-body file://./templates/iam-user-role.json --region $REGION --capabilities CAPABILITY_IAM
wait_for_stack "iam-user-role"