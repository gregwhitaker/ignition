import argparse
from colorama import Fore, init
import boto.iam
import boto.exception

class ReadonlyGroup:
    """
    Class responsible for adding and removing the readonly group.
    """
    __group_name = 'Readonly'
    __policy_name = 'Readonly'
    __policy_file_name = 'iam-readonly-group.json'

    def setup(self):
        """
        Creates the default readonly group and assigns the appropriate policy to the group.
        """
        conn = boto.iam.IAMConnection()

        conn.create_group(self.__group_name)
        conn.put_group_policy(self.__group_name, self.__policy_name, self.__load_policy("./policies/" + self.__policy_file_name))

        print(Fore.GREEN + "Created '" + Fore.YELLOW + self.__group_name + Fore.GREEN + "' group!" + Fore.RESET)

    def teardown(self):
        """
        Removes the default readonly group.
        """
        conn = boto.iam.IAMConnection()

        conn.delete_group_policy(self.__group_name, self.__policy_name)

        print(Fore.GREEN + "Removed '" + Fore.YELLOW + self.__group_name + Fore.GREEN + "' group policy!" + Fore.RESET)

        conn.delete_group(self.__group_name)

        print(Fore.GREEN + "Removed '" + Fore.YELLOW + self.__group_name + Fore.GREEN + "' group!" + Fore.RESET)

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

    parser = argparse.ArgumentParser(description="Adds or removes the readonly group from the account.")

    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument("-s", "--setup", help="Adds the readonly group to the account.", action="store_true")
    command_group.add_argument("-t", "--teardown", help="Removes the readonly group from the account.", action="store_true")

    args = parser.parse_args()

    readonly_group = ReadonlyGroup()

    if args.setup:
        readonly_group.setup()
    elif args.teardown:
        readonly_group.teardown()
    else:
        parser.error('No action requested, add --setup or --teardown')