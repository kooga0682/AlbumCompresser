#!/bin/bash

### Compress Audio from AIFF to FLAC ###
#
# This script compress all uncompressed audio file (such as .aif/.wav) in the album to FLAC format.
# The uncompressed audio in the directory will be removed after the end of processes.
# It is just a wrapper of FFmpeg.
#
#### This script is written for MacOSX ####



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
