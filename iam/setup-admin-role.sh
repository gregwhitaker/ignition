#! /bin/bash

#/ Usage: setup-admin-role
#/ Creates a role with administrator privileges.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

aws cloudformation create-stack --stack-name "iam-admin-role" --template-body file://./templates/iam-admin-role.json --region $REGION
wait_for_stack "iam-admin-role"