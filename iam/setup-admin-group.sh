#! /bin/bash

#/ Usage: setup-admin-group
#/ Creates a group with administrator privileges.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

# Creating Role
aws cloudformation create-stack --stack-name "iam-admin-group" --template-body file://./templates/iam-admin-group.json --region $REGION --capabilities CAPABILITY_IAM
wait_for_stack "iam-admin-group"