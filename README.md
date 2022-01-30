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
cd ~/Music/Library/Artist/Album
aifcomp
```


## Expected directory structure

### Before process
```
~/Music
└── Library
    ├── Artist A
    │   └── Album A
    │       ├── 01 music.aif
    │       └── 02 music.aif
    └── Artist B
        ├── Album B
        │   └── 01 music.mp4
        └── Album C
            ├── 01 music.mp4
            └── 02 music.mp4
```
### After process
```
~/Music
└── Library
    ├── Artist A
    │   └── Album A
    │       ├── 01 music.flac
    │       └── 02 music.flac
    └── Artist B
        ├── Album B
        │   └── 01 music.m4a
        └── Album C
            ├── 01 music.m4a
            └── 02 music.m4a
```