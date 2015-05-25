Identity and Access Management
===
AWS Identity and Access Management (IAM) enables you to securely control access to AWS services and resources for your users. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.

The IAM scripts can be used to configure the following:
* Account Alias
* Account Password Policy
* Administrator Group and Role
* User Group and Role
* Readonly Group and Role

##Account Settings
Configures policies that are applicable to the entire AWS account.

###setup-account-alias
Adds an account alias to the AWS account.  This allows you to refer to the account by a friendly name instead of the account number.

    $ ./setup-account-alias.sh <alias>
    
###teardown-account-alias
Removes the account alias from the AWS account.

    $ ./teardown-account-alias.sh <alias>

###setup-account-password-policy
Adds a default password policy to the AWS account.

	$ ./setup-account-password-policy.sh

###teardown-account-password-policy
Removes the default password policy from the AWS account.

	$ ./teardown-account-password-policy.sh

##Administrator Accounts
Configures groups and roles for administrator accounts. 

The adminstrator role has full access to the AWS API, including IAM management.

###setup-admin-role
Creates a role with administrator access to the AWS API, including IAM management.

	$ ./setup-admin-role.sh

###teardown-admin-role
Removes the administrator role.

	$ ./teardown-admin-role.sh

###setup-admin-group
Creates a group with the administrator role assigned to it by default.

	$ ./setup-admin-group.sh

###teardown-admin-group
Removes the administrator group.

	$ ./teardown-admin-group.sh

##User Accounts
Configures groups and roles for user accounts.  

The user role has full access to the AWS API, excluding IAM management.

###setup-user-role

###setup-user-group

##Readonly Accounts
Configures groups and roles for readonly accounts.

###setup-readonly-role

###setup-readonly-group