#! /bin/bash

#/ Usage: teardown-readonly-role
#/ Removes the readonly role.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

# Deleting Role
aws cloudformation delete-stack --stack-name "iam-readonly-role" --region $REGION