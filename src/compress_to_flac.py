#! python3

### Compress Audio from AIFF to FLAC ###
#
# This script compress all uncompressed audio file (such as .aif/.wav) in the album to FLAC format.
# The uncompressed audio in the directory will be removed after the end of processes.
# It is just a wrapper of FFmpeg.
#
#### This script is written for MacOSX ####

import subprocess
import os
import sys

def compress_to_flac(basename,extention):
    if os.path.isfile(basename+".flac"):
        print("Warning: "+basename+".flac alrady exists! Nothing to do for "+basename+extention,file=sys.stderr)
    else:
        subprocess.run("ffmpeg -i "+basename + extention + ' ' + basename + ".flac", shell=True)
    return

if __name__ == "__main__":
    # subprocess.run("echo subprocess test", shell=True)
    compress_to_flac("test")

'''
for UNCOMPRESSED_AUDIO in *.aif
do
    ## basename command was not working correct in shell script
    #basename $UNCOMPRESSED_AUDIO .aif
    #BASENAME=$( basename $UNCOMPRESSED_AUDIO .aif )
    
    BASENAME=${UNCOMPRESSED_AUDIO%.aif}
    #echo $BASENAME
    COMPRESSED_AUDIO=$BASENAME.flac
    #echo $COMPRESSED_AUDIO
    
    echo "Compressing $BASENAME ......   $UNCOMPRESSED_AUDIO -> $COMPRESSED_AUDIO"
    
    ffmpeg -y -i "$UNCOMPRESSED_AUDIO" "$COMPRESSED_AUDIO"
    rm "$BASENAME.aif"
    
done

echo -e "Done\n\n"
ls
'''
