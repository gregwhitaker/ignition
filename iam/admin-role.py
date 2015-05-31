import argparse
from colorama import Fore, init
import boto.iam
import boto.exception

class AdminRole:
    """
    Class responsible for adding and removing the administrator role.
    """
    __role_name = 'Administrator'
    __policy_name = 'Administrator'
    __policy_file_name = 'iam-admin-role.json'
    __assumerole_policy_file_name = 'iam-admin-assumerole.json'

    def setup(self):
        """
        Creates the default administrator role and assigns the appropriate policy to the role.
        """
        conn = boto.iam.IAMConnection()

        conn.create_role(self.__role_name, self.__load_policy("./policies/" + self.__assumerole_policy_file_name))
        conn.put_role_policy(self.__role_name, self.__policy_name, self.__load_policy("./policies/" + self.__policy_file_name))

        print(Fore.GREEN + "Created '" + Fore.YELLOW + self.__role_name + Fore.GREEN + "' role!" + Fore.RESET)

    def teardown(self):
        """
        Removes the default administrator role.
        """
        conn = boto.iam.IAMConnection()

        conn.delete_role_policy(self.__role_name, self.__policy_name)

        print(Fore.GREEN + "Removed '" + Fore.YELLOW + self.__role_name + Fore.GREEN + "' role policy!" + Fore.RESET)

        conn.delete_role(self.__role_name)

        print(Fore.GREEN + "Removed '" + Fore.YELLOW + self.__role_name + Fore.GREEN + "' role!" + Fore.RESET)

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

        # Initializing colorama because this method is currently being called
        # as a top-level script and not a module.
        init()
    else:
        from utils.logging import log_error

    parser = argparse.ArgumentParser(description="Adds or removes the administrator role from the account.")

    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument("-s", "--setup", help="Adds the administrator role to the account.", action="store_true")
    command_group.add_argument("-t", "--teardown", help="Removes the administrator role from the account.", action="store_true")

    args = parser.parse_args()

    admin_role = AdminRole()

    if args.setup:
        admin_role.setup()
    elif args.teardown:
        admin_role.teardown()
    else:
        parser.error('No action requested, add --setup or --teardown')