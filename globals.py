# Analog pins
ROTARY_PIN: int = 0

# Digital pins
LED_PIN: int = 4
BUZZER_PIN: int = 5
BUTTON_PIN: int = 6


SONG_LIST: list[dict[str, str]] = [
    {
        "name": "Mary Had A Little Lamb",
        "file": "songs/mary-had-a-little-lamb.csv"
    },
    {
        "name": "Yankee Doodle",
        "file": "songs/yankee-doodle.csv"
    },
    {
        "name": "Wheels on the Bus",
        "file": "songs/wheels-on-the-bus.csv"
    }
]

# Index of the song currently being played in SONG_LIST
g_current_song_index: int = -1

def function_to_make_this_module_import():
    """
    This function does nothing. It is only in here to make my editor shut up about not being able to resolve the import.
    """
    pass
