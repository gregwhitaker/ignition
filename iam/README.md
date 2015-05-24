Identity and Access Management
===
The IAM scripts can be used to configure the following:
* Account Alias
* Account Password Policy
* Administrator Group and Role
* User Group and Role
* Readonly Group and Role

##setup-account-alias
Adds an account alias to the AWS account.  This allows you to refer to the account by a friendly name and not the account number.

    ./setup-account-alias <alias>
    
##teardown-account-alias
Removes the account alias from the AWS account.

    ./teardown-account-alias <alias>
