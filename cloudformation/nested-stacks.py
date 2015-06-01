import argparse
from colorama import Fore, init

class NestedStacks:
    """
    Creates an S3 bucket to store CloudFormation Nested Stacks (reusable templates)
    """

    def __init__(self, bucket):
        """
        Initializes this instance of NestedStacks

        :param bucket: S3 bucket name
        """
        self.bucket = bucket

    def setup(self):
        """
        Creates an S3 bucket to store CloudFormation Nested Stacks
        """
        utils.s3.create_bucket(self.bucket)

    def teardown(self):
        """

        :return:
        """
        utils.s3.delete_bucket(self.bucket)


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from utils.logging import log_error
        import utils.s3

        # Initializing colorama because this method is currently being called
        # as a top-level script and not a module.
        init()
    else:
        from utils.logging import log_error
        import utils.s3

    parser = argparse.ArgumentParser(description="Adds or removes S3 bucket to hold Cloudformation Nested Stacks.")

    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument("-s", "--setup", help="Adds the S3 bucket to the account.", action="store_true")
    command_group.add_argument("-t", "--teardown", help="Removes the S3 bucket from the account.", action="store_true")

    parser.add_argument("--bucket", required=True, action="store", dest="bucket", help="S3 bucket name")

    args = parser.parse_args()

    nested_stacks = NestedStacks(args.bucket)

    if args.setup:
        nested_stacks.setup()
    elif args.teardown:
        nested_stacks.teardown()
    else:
        parser.error('No action requested, add --setup or --teardown')