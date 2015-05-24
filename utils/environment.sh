#! /bin/bash

DEFAULT_REGION=$(aws configure get region)

if [[ -z "$REGION" ]]; then
	export REGION=$DEFAULT_REGION
fi
