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
            print(Fore.Green + "Alias not specified, defaulting to '" + Fore.YELLOW + "master" + Fore.Green + "'" + Fore.RESET)
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
            # Check to see if the requested alias is already in use before creating the key
            aliases = conn.list_aliases()
            for alias in aliases['Aliases']:
                if alias['AliasName'] == 'alias/' + self.alias:
                    error = boto.kms.exceptions.AlreadyExistsException(400, 'AlreadyExistsException')
                    error.message = 'An alias with the name ' + alias['AliasArn'] + ' already exists'
                    raise error

            response = conn.create_key(self.__load_policy("./policies/kms-master-key.json"), 'Master Key')

            key_id = response['KeyMetadata']['KeyId']
            key_arn = response['KeyMetadata']['Arn']

            conn.create_alias("alias/" + self.alias, key_id)

            print(Fore.GREEN + "Added account master key '" + Fore.YELLOW + self.alias + Fore.GREEN + "' to region '" +
                  Fore.YELLOW + self.region + Fore.GREEN + "'" + Fore.RESET)
        except boto.exception.BotoServerError as error:
            log_error(error)
            raise

    def teardown(self):
        """
        Disables the default master encryption key.  Master keys cannot be deleted once they are created.
        """
        conn = boto.kms.connect_to_region(self.region)

        if conn is None:
            error = boto.exception.BotoServerError(404, "Not Found", message="KMS region " + self.region + " does not exist!")
            log_error(error)
            raise error

        try:
            aliases = conn.list_aliases()

            for alias in aliases['Aliases']:
                if alias['AliasName'] == 'alias/' + self.alias:
                    conn.delete_alias("alias/" + self.alias)
                    conn.disable_key(alias['TargetKeyId'])
                    break

            print(Fore.GREEN + "Disabled account master key '" + Fore.YELLOW + self.alias + Fore.GREEN + "' in region '" +
                  Fore.YELLOW + self.region + Fore.GREEN + "'" + Fore.RESET)
        except boto.exception.BotoServerError as error:
            log_error(error)
            raise

    def __load_policy(self, policy_path):
        with open(policy_path, "r") as policyFile:
            data = policyFile.read().replace('\n', '')

        self.__ensure_required_roles_created()

        admin_role_arn = self.required_roles['Administrator']
        user_role_arn = self.required_roles['User']
        account_number = admin_role_arn.lstrip("arn:aws:iam::").split(":").__getitem__(0).strip(" ")

        # Fill out the policy template with the appropriate ARNs
        data = data.replace("%%ADMINISTRATOR_ROLE_ARN%%", admin_role_arn)
        data = data.replace("%%USER_ROLE_ARN%%", user_role_arn)
        data = data.replace("%%ACCOUNT_NUMBER%%", account_number)

        return data

    def __ensure_required_roles_created(self):
        conn = boto.iam.IAMConnection()

        roles = conn.list_roles()

        self.required_roles = {}
        for role in roles.list_roles_result.roles:
            if role['role_name'] == 'Administrator':
                self.required_roles['Administrator'] = role['arn']
            elif role['role_name'] == 'User':
                self.required_roles['User'] = role['arn']

        # Create the Administrator role if it does not exist
        if not self.required_roles.__contains__('Administrator'):
            admin_role = AdminRole()
            response = admin_role.setup()

            self.required_roles['Administrator'] = response['arn']

        # Create the User role if it does not exist
        if not self.required_roles.__contains__('User'):
            user_role = UserRole()
            response = user_role.setup()

            self.required_roles['User'] = response['arn']


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

    parser.add_argument("--region", required=True, action="store", dest="region", help="AWS region")
    parser.add_argument("--alias", action="store", default="master", help="Master encryption key alias")

    args = parser.parse_args()

    master_key = MasterKey(args.region, args.alias)

    if args.setup:
        master_key.setup()
    elif args.teardown:
        master_key.teardown()
    else:
        parser.error('No action requested, add --setup or --teardown')
