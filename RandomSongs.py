import os
import random
import pygame
import time
import os
import random
import pygame
import time

def play_random_song(folder_path):
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print("Error: The specified folder does not exist.")
        return

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter only the files with supported extensions (e.g., mp3)
    supported_extensions = [".mp3", ".wav"]
    music_files = [file for file in files if os.path.splitext(file)[1].lower() in supported_extensions]

    # Check if there are any music files in the folder
    if not music_files:
        print("Error: No music files found in the specified folder.")
        return

    # Initialize pygame mixer
    pygame.mixer.init()

    # Select a random music file
    random_song = random.choice(music_files)
    print("Playing random song:", random_song)

    # Get the full path of the selected music file
    song_path = os.path.join(folder_path, random_song)

    # Load and play the music file
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    # Wait until the music finishes playing or the user enters 'q'
    while pygame.mixer.music.get_busy():
        user_input = input("Press 'q' to quit: ")
        if user_input.lower() == 'q':
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            return
        time.sleep(1)

if __name__ == "__main__":
    folder_path = "C:/Users/Infort/OneDrive/Desktop/Confidentials/Songs"
    play_random_song(folder_path)