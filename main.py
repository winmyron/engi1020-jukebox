from engi1020.arduino.api import *
from player import play_song
import song_parser as parser

SONG_LIST = [{
    "name": "Mary Had A Little Lamb",
    "file": "songs/mary-had-a-little-lamb.csv"
}]

if __name__ == "__main__":
    #print([i["name"] for i in SONG_LIST])
    #song_to_test = input("Type in a song to play: ")
    
    file_to_play: str = SONG_LIST[0]["file"]

    #for i in SONG_LIST:
    #    if song_to_test == i["name"]:
    #        file_to_play = i["file"]

    buzzer_instructions = parser.parse_song(file_to_play)
    play_song(buzzer_instructions)
