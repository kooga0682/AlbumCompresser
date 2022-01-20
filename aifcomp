#!/bin/bash

### Compress Audio from AIFF to FLAC ###

#### This script is written for MacOSX 



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
