import argparse
from colorama import Fore, init
import boto.iam
import boto.exception

class AccountPasswordPolicy:
    """
    Class responsible for adding and removing default account password policy.

    The default account password policy consists of the following settings:
        - Minimum Password Length: 8
        - Require Lowercase: True
        - Require Uppercase: True
        - Require Numbers: True
        - Require Symbols: True
        - Maximum Age: No Expiry
        - Allow Users to Change Password: True,
        - Password Reuse Prevention: 6 Most Recent Passwords
    """

    def setup(self):
        """
        Enables the default password policy on the account.
        """
        conn = boto.iam.IAMConnection()

        conn.update_account_password_policy(allow_users_to_change_password=True,
                                            max_password_age=90,
                                            password_reuse_prevention=6,
                                            minimum_password_length=8,
                                            require_lowercase_characters=True,
                                            require_uppercase_characters=True,
                                            require_numbers=True,
                                            require_symbols=True)

        print(Fore.GREEN + "Default Password Policy Enabled!" + Fore.RESET)

    def teardown(self):
        """
        Disables the default password policy on the account.
        """
        conn = boto.iam.IAMConnection()

        conn.delete_account_password_policy()

        print(Fore.GREEN + "Default Password Policy Disabled!" + Fore.RESET)

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from utils.logging import log_error

        # Initializing colorama because this method is currently being called
        # as a top-level script and not a module.
        init()
    else:
        from utils.logging import log_error

    parser = argparse.ArgumentParser(description="Adds or removes the default account password policy.")

    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument("-s", "--setup", help="Adds the default password policy to the account.", action="store_true")
    command_group.add_argument("-t", "--teardown", help="Removes the default password policy from the account.", action="store_true")

    args = parser.parse_args()

    account_password_policy = AccountPasswordPolicy()

    if args.setup:
        account_password_policy.setup()
    elif args.teardown:
        account_password_policy.teardown()
    else:
        parser.error('No action requested, add --setup or --teardown')