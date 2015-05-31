import argparse
from colorama import Fore, init
import boto.iam
import boto.kms
import boto.kms.layer1
import boto.exception
import boto.kms.exceptions

class MasterKey:
    """
    Class responsible for creating a default KMS master encryption key.
    """

    def __init__(self, region, alias):
        """
        Creates an instance of MasterKey.

        :type region: string
        :type alias: string
        :param region: AWS region
        :param alias: key alias (optional)
        :return: instance of MasterKey
        """
        if alias is None:
            self.alias = "master"
        else:
            self.alias = alias

        self.region = region

    def setup(self):
        """
        Creates the default master encryption key.
        """
        conn = boto.kms.connect_to_region(self.region)

        if conn is None:
            error = boto.exception.BotoServerError(404, "Not Found", message="KMS region " + self.region + " does not exist!")
            log_error(error)
            raise error

        # Master encryption key requires that both the Administrator and User roles have been created
        self.__ensure_required_roles_created()

        try:
            conn.create_key(self.__load_policy("./policies/kms-master-key.json"), 'Master Key')
            print(Fore.GREEN + "Added account alias '" + Fore.YELLOW + self.alias + Fore.GREEN + "'" + Fore.RESET)
        except boto.exception.BotoServerError as error:
            log_error(error)
            raise

    def teardown(self):
        """
        Disables the default master encryption key.  Master keys cannot be deleted once they are created.
        """
        try:
            print(Fore.GREEN + "Removed account alias '" + Fore.YELLOW + self.alias + Fore.GREEN + "'" + Fore.RESET)
        except boto.exception.BotoServerError as error:
            log_error(error)
            raise

    @staticmethod
    def __load_policy(policy_path):
        with open(policy_path, "r") as policyFile:
            data = policyFile.read().replace('\n', '')
        return data

    @staticmethod
    def __ensure_required_roles_created():
        conn = boto.iam.IAMConnection()
        roles = conn.list_roles()

        if not roles.__contains__('Administrator'):
            admin_role = AdminRole()
            admin_role.setup()

        if not roles.__contains__('User'):
            user_role = UserRole()
            user_role.setup()

    def __get_admin_arn(self):
        print ""

    def __get_user_arn(self):
        print ""

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from utils.logging import log_error
        from iam.admin_role import AdminRole
        from iam.user_role import UserRole

        # Initializing colorama because this method is currently being called
        # as a top-level script and not a module.
        init()
    else:
        from utils.logging import log_error
        from iam.admin_role import AdminRole
        from iam.user_role import UserRole

    parser = argparse.ArgumentParser(description="Adds or disables the default master encryption key for the account.")

    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument("-s", "--setup", help="Adds the default master encryption key to the account.", action="store_true")
    command_group.add_argument("-t", "--teardown", help="Disables the default master encryption key for the account.", action="store_true")

    parser.add_argument("--region", action="store", dest="region", help="AWS region")
    parser.add_argument("--alias", help="Master encryption key alias", default="master")

    args = parser.parse_args()

    master_key = MasterKey(args.region, args.alias)

    if args.setup:
        master_key.setup()
    elif args.teardown:
        master_key.teardown()
    else:
        parser.error('No action requested, add --setup or --teardown')
