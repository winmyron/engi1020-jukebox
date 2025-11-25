from engi1020.arduino.api import buzzer_note
from time import sleep

BUZZER_PIN = 5

# Be the wrapper that actually plays the music and allows for playback controls to be used.

def play_song(instructions):
    for i in instructions:
        freq, time = i
        play_line(freq, time)


def play_line(frequency, duration):
    buzzer_note(5, frequency, duration)
    sleep(duration)
