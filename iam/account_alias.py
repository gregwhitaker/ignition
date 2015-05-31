import argparse
from colorama import Fore, init
import boto.iam
import boto.exception

class AccountAlias:
    """
    Class responsible for adding and removing account aliases.
    """

    def __init__(self, alias):
        """
        Creates an instance of AccountAlias.

        :type alias: string
        :param alias: account alias
        :return: instance of AccountAlias
        """
        self.alias = alias

    def setup(self):
        """
        Creates the account alias.

        :type alias: string
        :param alias: account alias to create
        """
        conn = boto.iam.IAMConnection()

        try:
            conn.create_account_alias(self.alias)
            print(Fore.GREEN + "Added account alias '" + Fore.YELLOW + self.alias + Fore.GREEN + "'" + Fore.RESET)
        except boto.exception.BotoServerError as error:
            log_error(error)
            raise

    def teardown(self):
        """
        Removes the account alias.

        :type alias: string
        :param alias:
        """
        conn = boto.iam.IAMConnection()

        try:
            conn.delete_account_alias(self.alias)
            print(Fore.GREEN + "Removed account alias '" + Fore.YELLOW + self.alias + Fore.GREEN + "'" + Fore.RESET)
        except boto.exception.BotoServerError as error:
            log_error(error)
            raise

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

    parser = argparse.ArgumentParser(description="Adds or removes aliases from the account.")

    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument("-s", "--setup", help="Adds the alias to the account.", action="store_true")
    command_group.add_argument("-t", "--teardown", help="Removes the alias from the account.", action="store_true")

    parser.add_argument("--alias", required=True, action="store", dest="alias", help="The account alias")

    args = parser.parse_args()

    account_alias = AccountAlias(args.alias)

    if args.setup:
        account_alias.setup()
    elif args.teardown:
        account_alias.teardown()
    else:
        parser.error('No action requested, add --setup or --teardown')
