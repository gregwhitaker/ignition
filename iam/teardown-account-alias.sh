#! /bin/bash

source ../utils/logging.sh

log "Deleting Account Alias: $1"

aws iam delete-account-alias --account-alias $1