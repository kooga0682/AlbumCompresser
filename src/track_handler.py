import ffmpeg
import os
import shutil


def sort(track_path):
    extention = track_path.suffix
    # print(extention)

    if extention==".aif" or extention==".wav":
        processed_track_path = compress_to_flac(track_path)
    elif extention == ".mp4":
        processed_track_path = convert_to_m4a(track_path)
    else:
        processed_track_path = track_path

    return processed_track_path

def change_file_mode(track_path):
    track_path.chmod(0o644)
    return

def compress_to_flac(track_path):
    compressed_audio_path = track_path.with_suffix(".flac")
    # print("compress ",track_path," to ",compressed_audio_path)

    stream = ffmpeg.input(str(track_path))
    stream = ffmpeg.output(stream, str(compressed_audio_path))
    ffmpeg.run(stream, overwrite_output=True)
    move_to_trashbox(track_path)
    # subprocess.run("ffmpeg -i "+track_path + ' ' + basename + ".flac", shell=True)
    return compressed_audio_path


def convert_to_m4a(track_path):
    # print("convert ",track_path)
    # album_path = track_path.parent
    audio_file_path=track_path.with_suffix(".m4a")
    # print(audio_filename)
    # print(type(audio_filename))
    os.rename(track_path, audio_file_path)
    return audio_file_path


def move_to_trashbox(track):
    trashbox_path = track.parent.parent.parent.joinpath(".trashbox")
    create_trashbox(trashbox_path)

    moved = shutil.move(str(track), str(trashbox_path))
    # Path.unlink(missing_ok=False)

    return


def create_trashbox(trashbox_path):
    trashbox_path.mkdir(exist_ok=True)
    return
