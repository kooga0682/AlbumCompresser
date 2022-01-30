# Album Compresser

## Discription

This script compress all uncompressed audio file (such as .aif/.wav) in the album to FLAC format. The uncompressed audio in the directory will be removed after the end of processes.
It is just a wrapper of FFmpeg.


## Installation

### Mac
```
brew install ffmpeg
cp aifcomp.sh /usr/local/bin/aifcomp
cp rewriteextention.sh /usr/local/bin/rewriteextention
```

## Usage

### To compress aif to flac
```
cd PATH_OF_ALBUM
aifcomp
```

### To rewrite audio file extention from mp4 to m4a
```
cd PATH_OF_ALBUM
rewriteextention
```

### example
```
cd ~/Music/Album
aifcomp
```
