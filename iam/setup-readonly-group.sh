#! /bin/bash

#/ Usage: setup-readonly-group
#/ Creates a group with readonly privileges.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

# Creating Role
aws cloudformation create-stack --stack-name "iam-readonly-group" --template-body file://./templates/iam-readonly-group.json --region $REGION --capabilities CAPABILITY_IAM
wait_for_stack "iam-readonly-group"