#!/bin/bash

### Rewrite the file extension from mp4 to m4a ###

#### This script is written for MacOSX 

for MP4_FILE in *.mp4
do
    BASENAME=${MP4_FILE%.mp4}
    M4A_FILE=$BASENAME.m4a
    
    echo "Rewrite the extension of $BASENAME ......   $MP4_FILE -> $M4A_FILE"
    
    mv "$MP4_FILE" "$M4A_FILE"

done

echo -e "Done\n\n"
ls
