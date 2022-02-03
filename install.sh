#!/bin/bash

### This is a installation script of Audio Library Organizer ###
# 
# This script will place shell-scripts at /usr/local/bin
#
####

# Depends on OS
case "${OSTYPE}" in
  darwin* )
    # brew install ffmpeg
  ;;
  linux* )
  ;;
esac

# git clone https://github.com/kooga0682/AudioLibraryOrganizer.git

REPOSITORY_DIR="AudioLibraryOrganizer"
INSTALL_DIR="/usr/local/aifcomp"

cd REPOSITORY_DIR

for SCRIPT in *.sh
do

    BASENAME=${SCRIPT%.sh}

    echo "Copying $BASENAME to $INSTALL_DIR"
    
done
