#! /bin/bash

#/ Usage: teardown-admin-role
#/ Removes the administrator role.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

# Deleting Role
aws cloudformation delete-stack --stack-name "iam-admin-role" --region $REGION