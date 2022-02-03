#!/bin/bash

### In the Artist Directory, this script will compress all AIF file to FLAC and rewrite all .mp4 to .m4a ###

#### This script is written for MacOSX 

# I want to assign the current directory name to the ARTIST_NAME variable.
# But I can not use basename command because of spaces are exsisting in the name.
ARTIST_NAME=`pwd`  #${`pwd`%/*}

for ALBUM in *
do

    echo -e "Proccessing in $ALBUM ............\n\n"

    cd "$ALBUM"
    # aifcomp
    rewriteextention
    cd ..

    echo "================================================================================"

done

echo -e "All Processes of the "$ARTIST_NAME" have been done.\n"
