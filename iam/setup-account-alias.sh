#! /bin/bash

source ../utils/logging.sh

log "Creating Account Alias: $1"

aws iam create-account-alias --account-alias $1
