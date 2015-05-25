#! /bin/bash

#/ Usage: setup-master-key [alias]
#/ Creates a master encryption key in KMS.

source ../utils/environment.sh
source ../utils/logging.sh

# Defaulting key alias to "master" if an alias is not provided
if [ -z $1 ]; then
	ALIAS="master"
else
	ALIAS="$1"
fi

# Checking to see if the requested alias is already taken
OUTPUT=$(aws --output text kms list-aliases --region $REGION \
	| grep 'alias/$ALIAS')

if [ -n $OUTPUT ]; then
	echo "$(tput setaf 2)A key with alias '$(tput setaf 3)$ALIAS$(tput setaf 2)' already exists!$(tput sgr0)"
	exit 2
fi

# Creating the new master key
KEY_ID=$(aws --output text kms create-key --description "Master" \
	| grep 'KEYMETADATA' \
	| cut -f 7)

# Setting the alias on the newly created master key
aws kms create-alias --alias-name "alias/$ALIAS" --target-key-id "$KEY_ID" --region $REGION

echo "$(tput setaf 2)Generated '$(tput setaf 3)$ALIAS$(tput setaf 2)' Key: $(tput setaf 3)$KEY_ID$(tput sgr0)"