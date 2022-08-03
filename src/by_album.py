#! python3

### This script will process all files in the Album Directory.

import os
from compress_to_flac import compress_to_flac
import rewrite_extention
import change_file_mode


def main():
    files = os.listdir(".")

    for file in files:
        change_file_mode.change_mode(file)
        process_for(file)

def process_for(file):
    separated_file_name = os.path.splitext(file)
    basename            = separated_file_name[0]
    file_extension      = separated_file_name[1]

    # print(separated_file_name)
    if file_extension == '.mp4' :
        rewrite_extention.mp4_to_m4a(basename)
    elif file_extension == '.aif' or file_extension == '.wav':
        compress_to_flac(basename,file_extension)
    else :
        print("There is nothing to do for "+file)

if __name__ == "__main__":
    main()

main()