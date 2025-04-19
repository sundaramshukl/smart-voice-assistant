import os
import random

def play_music():
    music_dir = "your_music_directory_path"
    songs = os.listdir(music_dir)
    if songs:
        os.startfile(os.path.join(music_dir, random.choice(songs)))
