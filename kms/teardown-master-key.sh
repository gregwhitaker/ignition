#! /bin/bash

#/ Usage: teardown-master-key [alias]
#/ Disables a master encryption key in KMS.

source ../utils/environment.sh
source ../utils/logging.sh

# Defaulting key alias to "master" if an alias is not provided
if [ -z $1 ]; then
	ALIAS="master"
else
	ALIAS="$1"
fi

# Checking to see if the requested alias is already taken
KEY_ID=$(aws --output text kms list-aliases --region "$REGION" \
	| grep "alias/$ALIAS" \
	| cut -f 4)

if [ -z $KEY_ID ]; then
	echo "$(tput setaf 2)A key with alias '$(tput setaf 3)$ALIAS$(tput setaf 2)' cannot be found!$(tput sgr0)"
	exit 2
else
	# Disable the master key
	aws kms disable-key --key-id "$KEY_ID"
fi