#! python3

### Compress Audio from AIFF to FLAC ###
#
# This script compress all uncompressed audio file (such as .aif/.wav) in the album to FLAC format.
# The uncompressed audio in the directory will be removed after the end of processes.
# It is just a wrapper of FFmpeg.
#
#### This script is written for MacOSX ####

import os
import compress_to_flac
import rewrite_extention

files = os.listdir(".")

def main():
    files = os.listdir(".")

    for file in files:
        process_for(file)



def process_for(file):
    separated_file_name = os.path.splitext(file)
    basename            = separated_file_name[0]
    file_extension      = separated_file_name[1]
    
    # print(separated_file_name)
    if file_extension == '.mp4' :
        rewrite_extention.mp4_to_m4a(basename)
    elif file_extension == '.aif' :
        # print("Process for aif")
        compress_to_flac.aiff_to_flac(basename)
    else :
        print("There is nothing to do for "+file)

if __name__ == "__main__":
    main()
