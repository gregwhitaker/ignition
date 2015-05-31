import unittest
from iam.iam_utils import IAMUtils
from iam.admin_role import AdminRole

class TestIAMUtils(unittest.TestCase):

    def setUp(self):
        self.admin_role = AdminRole()
        self.admin_role.setup()

    def tearDown(self):
        self.admin_role.teardown()

    def test_administrator_account_is_created(self):
        utils = IAMUtils()
        self.assertTrue(utils.admin_role_exists())
