#! python3

### In the Artist Directory, this script will compress all AIF file to FLAC and rewrite all .mp4 to .m4a ###

import os
import by_album
import compress_to_flac
import rewrite_extention
import change_file_mode

files = os.listdir(".")

def main():
    directories = os.listdir(".")
    for directory in directories:
        if os.path.isfile(directory):
            
        elif os.path.isdir(file):
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
    elif file_extension == '.aif' :
        compress_to_flac.aiff_to_flac(basename)
    else :
        print("There is nothing to do for "+file)

if __name__ == "__main__":
    main()
