from engi1020.arduino.api import *
from time import sleep

from song_parser import parse_song

import globals
import ui


# Be the wrapper that actually plays the music and allows for playback controls to be used.

def play_song(song):
    # TODO: CONSULT SONG LIST
    
    oled_clear()
    oled_print(f"Now Playing: {song["name"]}")

    instructions = parse_song(song["file"])

    for i in instructions:
        # Pausing
        button_input = digital_read(globals.BUTTON_PIN)
        is_paused = False
        
        # Skipping
        skip_forwards_input: bool
        skip_backwards_input: bool

        if button_input == False:
            is_paused = toggle_pause(is_paused)

        while is_paused:
            button_input = digital_read(globals.BUTTON_PIN)

            if button_input == True:
                is_paused = toggle_pause(is_paused)



        freq, time = i
        play_line(freq, time)


def play_line(frequency, duration):
    buzzer_note(globals.BUZZER_PIN, frequency, duration)
    sleep(duration)


def toggle_pause(pause_state) -> bool:
    if pause_state == False:
        digital_write(globals.BUZZER_PIN, True)
        oled_clear()
        oled_print("Song paused")
        sleep(0.25)
        return True
    else:
        digital_write(globals.BUZZER_PIN, False)
        oled_clear()
        oled_print(f"Now Playing: {globals.SONG_LIST[globals.g_current_song_index]["name"]}")
        sleep(0.2)
        return False
