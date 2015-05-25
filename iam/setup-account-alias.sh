#! /bin/bash

#/ Usage: setup-account-alias <alias>
#/ Creates an alias for the AWS account.

source ../utils/logging.sh

usage() {
	echo "Usage: setup-account-alias <alias>"
}

if [ -z "$1" ]; then
	echo "Alias is required!"
	usage
	exit 1
fi

aws iam create-account-alias --account-alias $1
