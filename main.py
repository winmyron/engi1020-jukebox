from engi1020.arduino.api import *
import globals
import player
import song_parser as parser
import ui
from time import sleep


def play_song(instructions):
    """
    Handles everything that occurs during playback of a song, including
    - Playback
    - Pausing
    """
    for i in instructions:
        # Pausing
        button_input = digital_read(globals.BUTTON_PIN)
        is_paused = False
        
        # Pauses if button is pressed
        if button_input == True:
            is_paused = player.toggle_pause(is_paused)

        # Loops until button is pressed again to unpause. This is the "paused" state
        while is_paused:
            button_input = digital_read(globals.BUTTON_PIN)

            if button_input == True:
                is_paused = player.toggle_pause(is_paused)

        freq, time = i
        player.play_line(freq, time)


if __name__ == "__main__":
    while True:
        current_song_index = 0
        while globals.g_current_song_index == -1:
            pot_input = analog_read(globals.ROTARY_PIN)
            button_input = digital_read(globals.BUTTON_PIN)
            print(pot_input)
            print(current_song_index)

            ui.display_menu(current_song_index)

            # Menu navigation with potentiometer input
            # Includes bidirectional index rollover
            if pot_input < 400:
                if current_song_index == 0:
                    current_song_index = len(globals.SONG_LIST) - 1
                else:
                    current_song_index -= 1
            elif pot_input > 600:
                if current_song_index == len(globals.SONG_LIST) - 1:
                    current_song_index = 0 
                else:
                    current_song_index += 1

            sleep(1)

            if button_input == True:
                globals.g_current_song_index = current_song_index
        
        # The fun part: Getting the song to be played and actually playing it
        file_to_play: str = globals.SONG_LIST[globals.g_current_song_index]["file"]
        buzzer_instructions = parser.parse_song(file_to_play)
        play_song(buzzer_instructions)

        # Resets index to return to menu after song has played
        globals.g_current_song_index = -1
