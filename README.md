# Audio Library Organizer

## Discription

This software will organize your Audio Library.
Following processes will apply to all files in the library directory.

- Uncompressed file (now only .aif) will compress to FLAC.
- .mp4 containerized audio file will rename to .m4a

## Requirement

- ffmppeg

## Installation

### Preinstallation
```sh

brew install ffmpeg
```

### Mac
```sh
brew install ffmpeg
git clone https://github.com/kooga0682/AudioLibraryOrganizer.git
cp AudioLibraryOrganizer/aifcomp.sh /usr/local/bin/aifcomp
cp AudioLibraryOrganizer/rewriteextention.sh /usr/local/bin/rewriteextention
```

## Usage

### To compress aif to flac
```sh
cd PATH_OF_ALBUM
aifcomp
```

### To rewrite audio file extention from mp4 to m4a
```sh
cd PATH_OF_ALBUM
rewriteextention
```

### example
```sh
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