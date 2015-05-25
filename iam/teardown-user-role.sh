#! /bin/bash

#/ Usage: teardown-user-role
#/ Removes the user role.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

# Deleting Role
aws cloudformation delete-stack --stack-name "iam-user-role" --region $REGION