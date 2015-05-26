#! /bin/bash

#/ Usage: teardown-account-password-policy
#/ Removes the account password policy.

source ../utils/logging.sh

# Deleting the Password Policy
aws iam delete-account-password-policy

log_green "Password Policy Removed!"