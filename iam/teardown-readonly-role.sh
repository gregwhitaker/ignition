#! /bin/bash

#/ Usage: teardown-readonly-role
#/ Removes the readonly role.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

# Retrieve the name of the role from CloudFormation
find_resource_created_by_cloudformation "iam-readonly-role" "ReadonlyRole"

if [ -n "$CF_RESX" ]; then
	# Deleting Role
	aws cloudformation delete-stack --stack-name "iam-readonly-role" --region $REGION

	echo "$(tput setaf 2)Removed IAM Role: $(tput setaf 3)$CF_RESX$(tput sgr0)"
	exit 0
else
	echo "$(tput setaf 2)The '$(tput setaf 3)ReadonlyRole$(tput setaf 2)' role does not exist!$(tput sgr0)"
	exit 0
fi