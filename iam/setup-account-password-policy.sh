#! /bin/bash

#/ Usage: setup-account-password-policy
#/ Sets the account password policy to the following:
#/   - Minimum Password Length: 8
#/	 - Require Symbols: Yes
#/   - Require Numbers: Yes
#/   - Require Uppercase: Yes
#/   - Require Lowercase: Yes
#/   - Maximum Age: No Expiry
#/   - Allow Users to Change Password: Yes
#/   - Password Reuse Prevention: 6 Most Recent Passwords

source ../utils/logging.sh

# Creating the Password Policy
aws iam update-account-password-policy \
	--minimum-password-length 8 \
	--require-symbols \
	--require-numbers \
	--require-uppercase-characters \
	--require-lowercase-characters \
	--allow-users-to-change-password \
	--password-reuse-prevention 6

log_green "New Password Policy Configured!"