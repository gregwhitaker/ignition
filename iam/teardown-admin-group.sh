#! /bin/bash

#/ Usage: teardown-admin-group
#/ Removes the administrator group.

source ../utils/environment.sh
source ../utils/logging.sh
source ../utils/cloudformation.sh

# Retrieve the name of the group from CloudFormation
find_resource_created_by_cloudformation "iam-admin-group" "AdminGroup"

if [ -n "$CF_RESX" ]; then
	# Deleting Group
	aws cloudformation delete-stack --stack-name "iam-admin-group" --region $REGION

	echo "$(tput setaf 2)Removed IAM Group: $(tput setaf 3)$CF_RESX$(tput sgr0)"
	exit 0
else
	echo "$(tput setaf 2)The '$(tput setaf 3)AdminGroup$(tput setaf 2)' group does not exist!$(tput sgr0)"
	exit 0
fi