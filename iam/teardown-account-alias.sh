#! /bin/bash

#/ Usage: teardown-account-alias <alias>
#/ Creates an alias for the AWS account.

source ../utils/logging.sh

usage() {
	echo "Usage: teardown-account-alias <alias>"
}

if [ -z "$1" ]; then
	echo "Alias is required!"
	usage
	exit 1
fi

# Deleting Account Alias
aws iam delete-account-alias --account-alias $1

if [ $? == 0 ]; then
	echo "$(tput setaf 2)Deleted Account Alias: $(tput setaf 3)$1$(tput sgr0)"
	exit 0
else
	echo "$(tput setaf 2)Alias '$(tput setaf 3)$1$(tput setaf 2)' does not exist!$(tput sgr0)"
	exit 1
fi