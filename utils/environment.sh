#! /bin/bash

#/ This script checks to see if the AWS CLI "REGION" environment variable has been set.  If not, this
#/ script sets the environment variable to the default region specified in the user's AWS credentials file.

DEFAULT_REGION=$(aws configure get region)

if [[ -z "$REGION" ]]; then
	export REGION=$DEFAULT_REGION
fi