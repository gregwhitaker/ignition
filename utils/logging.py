from colorama import Fore, Back, Style
import boto.exception

def log_error(error):
    """

    :param error: boto.exception.BotoServerError
    :return:
    """
    print(Fore.RED + "Error occured: " + error.message + Fore.RESET)