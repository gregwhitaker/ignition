#! /bin/bash

#/ Usage: setup-readonly-role
#/ Creates a role with readonly privileges.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

# Creating Role
aws cloudformation create-stack --stack-name "iam-readonly-role" --template-body file://./templates/iam-readonly-role.json --region $REGION
wait_for_stack "iam-readonly-role"