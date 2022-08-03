#! python3

################################################################################
#
### This software organizes audio files to load in DAP  ###
### This software is written for Mac/Linux
#
################################################################################

import os
# from pathlib import Path
from pathlib import PosixPath
# import by_artist
import compress_to_flac
# import rewrite_extention
# import change_file_mode
import track_handler

# files = os.listdir(".")

def by_album(album):
    # print(album)
    tracks = [x for x in album.iterdir() if x.is_file()]
    for track in tracks:
        # print(track)
        processed_track = track_handler.sort(track)
        track_handler.change_file_mode(processed_track)
    
    album.chmod(0o755)
    return


def by_artist(artist):
    # print(artist.iterdir() )
    albums = [x for x in artist.iterdir() if x.is_dir()]
    for album in albums:
        # print(album)
        by_album(album)
    artist.chmod(0o755)
    return

def main():
    ### Set the audio library directory ########################################
    audio_library_relative_path = "~/Music/Library"
    # audio_library_relative_path = "./test"
    p = PosixPath(audio_library_relative_path)
    expanded_path = p.expanduser()
    audio_library_absolute_path = expanded_path.absolute()
    # print(audio_library_path)

    # Get the list of sub directories


    artists = [x for x in audio_library_absolute_path.iterdir() if x.is_dir()]
    
    # artists = os.listdir(audio_library_path)
    # print(os.path.isdir(artists[3]))

    for artist in artists:
        # print(artist,os.path.isdir(artist))
        by_artist(artist)

    return


if __name__ == "__main__":
    main()
