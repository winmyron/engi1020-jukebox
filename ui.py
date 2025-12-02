from engi1020.arduino import joystick
from engi1020.arduino.api import *
from time import sleep
import globals


# Displays info about the song currently playing
def display_song_info(song):
    oled_clear()
    oled_print(f"Now playing: {song["name"]}")


# Displays the menu of songs to play
def display_menu(selected_index):
    oled_clear()
    oled_print("")
    for i, song in enumerate(globals.SONG_LIST):
        if i == selected_index:
            oled_print(f"> {song["name"]}") # highlights the song
            print(f"> {song["name"]}")
        else:
            oled_print(f"{song["name"]}")
            print(f"{song["name"]}")
