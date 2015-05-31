import os
import boto.iam
import boto.exception
from admin_role import AdminRole
from user_role import UserRole
from readonly_role import ReadonlyRole

class IAMUtils:
    """
    Utility methods useful for interacting with IAM roles.
    """

    def __init__(self):
        """
        Initializes this instance of IAMUtils.
        """
        self.conn = boto.iam.IAMConnection()

    def admin_role_exists(self):
        """

        :return:
        """
        return self.conn.list_roles().__contains__(AdminRole.role_name)

    def user_role_exists(self):
        """

        :return:
        """
        return self.conn.list_roles().__contains__(UserRole.role_name)

    def readonly_role_exists(self):
        """

        :return:
        """
        return self.conn.list_roles().__contains__(ReadonlyRole.role_name)

    def get_admin_role_arn(self):
        """

        :return:
        """
        if self.admin_role_exists():
            role = self.conn.get_role(AdminRole.role_name)
            print role
        else:
            return None

    def get_user_role_arn(self):
        """

        :return:
        """
        if self.user_role_exists():
            role = self.conn.get_role(UserRole.role_name)
            print role
        else:
            return None

    def get_readonly_role_arn(self):
        """

        :return:
        """
        if self.readonly_role_exists():
            role = self.conn.get_role(ReadonlyRole.role_name)
            print role
        else:
            return None

    def load_policy(self, policy_file_name):
        """

        :param policy_file_name:
        :return:
        """
        policy_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir, 'iam')) + "/policies/" + policy_file_name
        with open (policy_path, "r") as policyFile:
            data = policyFile.read().replace('\n', '')

        return data