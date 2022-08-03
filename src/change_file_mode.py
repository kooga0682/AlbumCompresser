#! python3

## This script will change file/directory mode as the following.
# File      : -rw-r--r--
# Directory : drwxr-xr-x

import subprocess
import os

def change_mode(file):
    if os.path.isfile(file) :
        os.chmod(file, 0o644)
        # subprocess.run(["echo","chmod 644"+file], shell=True)
        # subprocess.Popen("chmod 644 "+file, shell=True)
    elif os.path.isdir(file):
        os.chmod(file, 0o755)
        # subprocess.run("chmod 755 "+file, shell=True)

    return

if __name__ == "__main__":
    change_mode("test test")
