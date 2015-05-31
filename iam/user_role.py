import os
import argparse
from colorama import Fore, init
import boto.iam
import boto.exception

class UserRole:
    """
    Class responsible for adding and removing the user role.
    """
    role_name = 'User'
    __policy_name = 'User'
    __policy_file_name = 'iam-user-role.json'
    __assumerole_policy_file_name = 'iam-user-assumerole.json'

    def setup(self):
        """
        Creates the default user role and assigns the appropriate policy to the role.
        """
        conn = boto.iam.IAMConnection()

        role = conn.create_role(self.role_name, self.load_policy(self.__assumerole_policy_file_name))
        conn.put_role_policy(self.role_name, self.__policy_name, self.load_policy(self.__policy_file_name))

        print(Fore.GREEN + "Created '" + Fore.YELLOW + self.role_name + Fore.GREEN + "' role!" + Fore.RESET)

        return dict([('id', role.create_role_result.role['role_id']),
                     ('name', role.create_role_result.role['role_name']),
                     ('arn', role.create_role_result.role['arn'])])

    def teardown(self):
        """
        Removes the default user role.
        """
        conn = boto.iam.IAMConnection()

        conn.delete_role_policy(self.role_name, self.__policy_name)

        print(Fore.GREEN + "Removed '" + Fore.YELLOW + self.role_name + Fore.GREEN + "' role policy!" + Fore.RESET)

        conn.delete_role(self.role_name)

        print(Fore.GREEN + "Removed '" + Fore.YELLOW + self.role_name + Fore.GREEN + "' role!" + Fore.RESET)

    def load_policy(self, policy_file_name):
        """

        :param policy_file_name:
        :return:
        """
        policy_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir, 'iam')) + "/policies/" + policy_file_name
        with open (policy_path, "r") as policyFile:
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

    parser = argparse.ArgumentParser(description="Adds or removes the user role from the account.")

    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument("-s", "--setup", help="Adds the user role to the account.", action="store_true")
    command_group.add_argument("-t", "--teardown", help="Removes the user role from the account.", action="store_true")

    args = parser.parse_args()

    user_role = UserRole()

    if args.setup:
        user_role.setup()
    elif args.teardown:
        user_role.teardown()
    else:
        parser.error('No action requested, add --setup or --teardown')