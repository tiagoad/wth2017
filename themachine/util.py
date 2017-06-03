import os
import subprocess
import tempfile


def tmp_dir(prefix):
    prefix = prefix if prefix else 'machine_'

    # create temporary directory if it doesn't exist
    os.makedirs(os.getenv('TMP_DIR'), exist_ok=True)

    # create and return temporary directory
    return tempfile.mkdtemp(prefix=prefix + '_', dir=os.getenv('TMP_DIR'))

def exec(args):
    return subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def load_config(filename):
    pass
