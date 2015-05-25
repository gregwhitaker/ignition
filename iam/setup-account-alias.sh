#! /bin/bash

#/ Usage: setup-account-alias <alias>
#/ Creates an alias for the AWS account.

source ../utils/logging.sh

usage() {
	echo "Usage: setup-account-alias <alias>"
}

if [ -z "$1" ]; then
	log_green "Alias is required!"
	usage
	exit 1
fi

# Creating Account Alias
aws iam create-account-alias --account-alias $1

if [ $? == 0 ]; then
	echo "$(tput setaf 2)Created Account Alias: $(tput setaf 3)$1$(tput sgr0)"
else
	echo "$(tput setaf 2)Alias '$(tput setaf 3)$1$(tput setaf 2)' already exists!$(tput sgr0)"
fi