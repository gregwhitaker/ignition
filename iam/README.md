# Identity and Access Management
AWS Identity and Access Management (IAM) enables you to securely control access to AWS services and resources for your users. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.

The IAM scripts can be used to configure the following:
* Account Alias
* Account Password Policy
* Administrator Group and Role
* User Group and Role
* Readonly Group and Role

## Account Settings
Configures policies that are applicable to the entire AWS account.

### Setup Account Alias
Adds an account alias to the AWS account.  This allows you to refer to the account by a friendly name instead of the account number.

    $ python account_alias.py --setup --alias ALIAS
    
### Teardown Account Alias
Removes the account alias from the AWS account.

    $ python account_alias.py --teardown --alias ALIAS

### Setup Account Password Policy
Adds a default password policy to the AWS account.

    $ python account_password_policy.py --setup

The default password policy is:

* Minimum password length of 8 characters
* Require at least one special character
* Require at least one number
* Require at least one uppercase letter
* Require at least one lowercase letter
* No password expiry
* User's are allowed to change their passwords
* User's new passwords cannot match their 6 most recent passwords

### Teardown Account Password Policy
Removes the default password policy from the AWS account.

    $ python account_password_policy.py --teardown

## Administrator Accounts
Configures groups and roles for administrator accounts. 

* Adminstrator accounts have full access to the AWS API, including IAM management.

### Setup Adminstrator Role
Creates a role with administrator access to the AWS API, including IAM management.

    $ python admin-role.py --setup

### Teardown Administrator Role
Removes the administrator role.

    $ python admin-role.py --teardown

### Setup Administrator Group
Creates a group with the administrator role assigned to it by default.

    $ python admin-group.py --setup

### Teardown Administrator Group
Removes the administrator group.

    $ python admin-group.py --teardown

## User Accounts
Configures groups and roles for user accounts.  

* User accounts have full access to the AWS API, excluding IAM management.

### Setup User Role
Creates a role with full access to the AWS API, excluding IAM management.

    $ python user-role.py --setup

### Teardown User Role
Removes the user role.

    $ python user-role.py --teardown

### Setup User Group
Creates a group with the user role assigned to it by default.

    $ python user-group.py --setup

### Teardown User Group
Removes the user group.

    $ python user-group.py --teardown

## Readonly Accounts
Configures groups and roles for readonly accounts.

* Readonly accounts have readonly access to the AWS API.

### Setup Readonly Role
Creates a role with readonly access to the AWS API.

    $ python readonly-role.py --setup

### Teardown Readonly Role
Removes the readonly role.

    $ python readonly-role.py --teardown

### Setup Readonly Group
Creates a group with the readonly role assigned to it by default.

    $ python readonly-group.py --setup

### Teardown Readonly Group
Removes the readonly group.

    $ python readonly-group.py --teardown
