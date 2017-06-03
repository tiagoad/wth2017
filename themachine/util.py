import os
import subprocess
import tempfile


def tmp_dir(prefix):
    """
    Creates a temporary directory

    :param prefix:  Prefix to add before the random directory name
    :return:        Absolute directory path
    """
    prefix = prefix if prefix else 'machine_'

    # create temporary directory if it doesn't exist
    os.makedirs(os.getenv('TMP_DIR'), exist_ok=True)

    # create and return temporary directory
    return tempfile.mkdtemp(prefix=prefix + '_', dir=os.getenv('TMP_DIR'))

def exec(args):
    """
    Subprocess.run wrapper

    :param args:    Command line arguments, a list.
    :return:        See documentation for subprocess.run
    """
    return subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
