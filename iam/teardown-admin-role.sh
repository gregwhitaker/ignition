#! /bin/bash

#/ Usage: teardown-admin-role
#/ Removes the administrator role.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

# Retrieve the name of the role from CloudFormation
find_resource_created_by_cloudformation "iam-admin-role" "AdminRole"

if [ -n "$CF_RESX" ]; then
	# Deleting Role
	aws cloudformation delete-stack --stack-name "iam-admin-role" --region $REGION

	echo "$(tput setaf 2)Removed IAM Role: $(tput setaf 3)$CF_RESX$(tput sgr0)"
	exit 0
else
	echo "$(tput setaf 2)The '$(tput setaf 3)AdminRole$(tput setaf 2)' role does not exist!$(tput sgr0)"
	exit 0
fi
