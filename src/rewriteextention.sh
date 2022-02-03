#!/bin/bash

### Rewrite the file extension from mp4 to m4a ###

#### This script is written for MacOSX 

# I want to assign the current directory name to the ALBUM_NAME variable.
# But I can not use basename command because of spaces are exsisting in the name.
ALBUM_NAME=`pwd`  #${`pwd`%/*}

for MP4_FILE in *.mp4
do
    BASENAME=${MP4_FILE%.mp4}
    M4A_FILE=$BASENAME.m4a
    
    echo "Rewrite the extension of $BASENAME ......   $MP4_FILE -> $M4A_FILE"
    
    mv "$MP4_FILE" "$M4A_FILE"

done

echo -e "All Processes of the "$ALBUM_NAME" have been done.\n"
