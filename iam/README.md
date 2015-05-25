Identity and Access Management
===
AWS Identity and Access Management (IAM) enables you to securely control access to AWS services and resources for your users. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.

The IAM scripts can be used to configure the following:
* Account Alias
* Account Password Policy
* Administrator Group and Role
* User Group and Role
* Readonly Group and Role

##setup-account-alias
Adds an account alias to the AWS account.  This allows you to refer to the account by a friendly name instead of the account number.

    $ ./setup-account-alias.sh <alias>
    
##teardown-account-alias
Removes the account alias from the AWS account.

    $ ./teardown-account-alias.sh <alias>
