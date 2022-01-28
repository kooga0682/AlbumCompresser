# Album Compresser

## Discription

This script compress all uncompressed audio file (such as .aif/.wav) in the album to FLAC format. The uncompressed audio in the directory will be removed after the end of processes.
It is just a wrapper of FFmpeg.


## Installation

### Mac
```
brew install ffmpeg
cp aifcomp /usr/local/bin
```

## Usage

```
cd PATH_OF_ALBUM
aifcomp
```


### example
```
cd ~/Music/Album
aifcomp
```