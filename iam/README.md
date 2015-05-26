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

The default password policy is:

* Minimum password length of 8 characters
* Require at least one special character
* Require at least one number
* Require at least one uppercase letter
* Require at least one lowercase letter
* No password expiry
* User's are allowed to change their passwords
* User's new passwords cannot match their 6 most recent passwords

###teardown-account-password-policy
Removes the default password policy from the AWS account.

	$ ./teardown-account-password-policy.sh

##Administrator Accounts
Configures groups and roles for administrator accounts. 

* Adminstrator accounts have full access to the AWS API, including IAM management.

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

* User accounts have full access to the AWS API, excluding IAM management.

###setup-user-role
Creates a role with full access to the AWS API, excluding IAM management.

	$ ./setup-user-role.sh

###teardown-user-role
Removes the user role.

	$ ./teardown-user-role.sh

###setup-user-group
Creates a group with the user role assigned to it by default.

	$ ./setup-user-group.sh

###teardown-user-role
Removes the user group.

	$ ./teardown-user-group.sh

##Readonly Accounts
Configures groups and roles for readonly accounts.

* Readonly accounts have readonly access to the AWS API.

###setup-readonly-role
Creates a role with readonly access to the AWS API.

	$ ./setup-readonly-role.sh

###teardown-readonly-role
Removes the readonly role.

	$ ./teardown-readonly-role.sh

###setup-readonly-group
Creates a group with the readonly role assigned to it by default.

	$ ./setup-readonly-group.sh

###teardown-readonly-group
Removes the readonly group.

	$ ./teardown-readonly-group.sh