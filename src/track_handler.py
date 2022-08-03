
from email.mime import audio
import subprocess
import os

def sort(track_path):
    extention = track_path.suffix
    # print(extention)

    if extention == ".aif" or extention==".wav":
        compress_to_flac(track_path)
    elif extention == ".mp4":
        convert_to_m4a(track_path)
    return


def compress_to_flac(track_path):
    print("compress ",track_path)
    return


def convert_to_m4a(track_path):
    # print("convert ",track_path)
    # album_path = track_path.parent
    audio_file_path=track_path.with_suffix(".m4a")
    # print(audio_filename)
    # print(type(audio_filename))
    os.rename(track_path, audio_file_path)
    return
