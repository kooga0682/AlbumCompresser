#! python3

### Rewrite the file extension from mp4 to m4a ###

#### This script is written for MacOSX 


import os
import sys

def mp4_to_m4a(filename):
    if os.path.isfile(filename+".m4a"):
        print("Warning: "+filename+".m4a alrady exists! Nothing to do for "+filename+".mp4",file=sys.stderr)
    else:
        os.rename(filename+".mp4", filename+".m4a")
    return

if __name__ == "__main__":
    mp4_to_m4a("test")
