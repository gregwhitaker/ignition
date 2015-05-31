import argparse
from colorama import Fore, init
import boto.iam
import boto.exception

class ReadonlyRole:
    """
    Class responsible for adding and removing the readonly role.
    """
    role_name = 'Readonly'
    __policy_name = 'Readonly'
    __policy_file_name = 'iam-readonly-role.json'
    __assumerole_policy_file_name = 'iam-readonly-assumerole.json'

    def setup(self):
        """
        Creates the default readonly role and assigns the appropriate policy to the role.
        """
        conn = boto.iam.IAMConnection()

        iamutils = IAMUtils()

        conn.create_role(self.role_name, iamutils.load_policy(self.__assumerole_policy_file_name))
        conn.put_role_policy(self.role_name, self.__policy_name, iamutils.load_policy(self.__policy_file_name))

        print(Fore.GREEN + "Created '" + Fore.YELLOW + self.role_name + Fore.GREEN + "' role!" + Fore.RESET)

    def teardown(self):
        """
        Removes the default readonly role.
        """
        conn = boto.iam.IAMConnection()

        conn.delete_role_policy(self.role_name, self.__policy_name)

        print(Fore.GREEN + "Removed '" + Fore.YELLOW + self.role_name + Fore.GREEN + "' role policy!" + Fore.RESET)

        conn.delete_role(self.role_name)

        print(Fore.GREEN + "Removed '" + Fore.YELLOW + self.role_name + Fore.GREEN + "' role!" + Fore.RESET)

    def __load_policy(self, path):
        with open (path, "r") as policyFile:
            data = policyFile.read().replace('\n', '')

        return data

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from utils.logging import log_error
        from iam_utils import IAMUtils


        # Initializing colorama because this method is currently being called
        # as a top-level script and not a module.
        init()
    else:
        from utils.logging import log_error
        from iam_utils import IAMUtils

    parser = argparse.ArgumentParser(description="Adds or removes the readonly role from the account.")

    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument("-s", "--setup", help="Adds the readonly role to the account.", action="store_true")
    command_group.add_argument("-t", "--teardown", help="Removes the readonly role from the account.", action="store_true")

    args = parser.parse_args()

    readonly_role = ReadonlyRole()

    if args.setup:
        readonly_role.setup()
    elif args.teardown:
        readonly_role.teardown()
    else:
        parser.error('No action requested, add --setup or --teardown')