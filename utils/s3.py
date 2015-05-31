
def is_bucket(name):
    """

    :param name:
    :return:
    """
    return True


def delete_bucket(name):

    if is_bucket(name):
        flush_bucket(name)

    print ""


def flush_bucket(name):
    if is_bucket(name):
        print ""
    print ""
