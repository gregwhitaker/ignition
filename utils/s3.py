import boto.s3
import boto.s3.connection
import boto.s3.acl

def is_bucket(name, region):
    """
    Checks to see if an S3 bucket exists with a given name.

    :type name: string
    :param name: bucket name
    :return: True if the bucket exists; otherwise False
    """
    conn = boto.s3.connect_to_region(region)
    if not conn.lookup(name) is None:
        return True
    else:
        return False


def create_bucket(name, region, **kwargs):
    """
    Creates a new S3 bucket.

    :param name:
    :param region:
    :return:
    """
    conn = boto.s3.connect_to_region(region)
    conn.create_bucket(name)


def delete_bucket(name, region, **kwargs):
    """
    Deletes an existing S3 bucket.

    :param name:
    :return:
    """
    if is_bucket(name):
        if not kwargs['flush'] is None and kwargs['flush'] is True:
            flush_bucket(name, region)

        conn = boto.s3.connect_to_region(region)
        conn.delete_bucket(name)


def flush_bucket(name, region):
    """
    Flushes an existing S3 bucket.

    :param name:
    :return:
    """
    if is_bucket(name, region):
        conn = boto.s3.connect_to_region(region)
        bucket = boto.s3.connection.Bucket(conn, name)

        for folder in bucket.list():
            bucket.delete_key(folder.key)

