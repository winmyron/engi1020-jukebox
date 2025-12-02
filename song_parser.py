import csv

NOTE_BASE_FREQUENCIES: dict[str, float] = {
    "C": 16.35,
    "C#": 17.32,
    "D": 18.35,
    "D#": 19.45,
    "E": 20.6,
    "F": 21.83,
    "F#": 23.12,
    "G": 24.5,
    "G#": 25.96,
    "A": 27.5,
    "A#": 29.14,
    "B": 30.87,
}

# Octaves are exactly double or half one another. Therefore we can multiply the above by 2^x, where x is the octave.

def get_note_duration(tempo: float, beat_note: int, note_type: int, note_count: int) -> float:
    """
    Gets the duration of a note using a formula, t = nm/f^2, where
        t = time (s)
        n = # of notes
        m = note type, as a fraction of the duration of the note that gets the beat
        f = tempo (Hz)
    """

    m = beat_note / note_type
    f = tempo * (1 / 60) # Convert from BPM to Hz

    t = (note_count * m) / f**2 # Duration

    return t


def get_note_frequency(note: str) -> int:
    """
    Gets the frequency to play from the note by taking the base frequency of the note and multiplying it by 2^octave
    """
    octave: int = int(note[-1])

    note_name: str = note[:-1]

    frequency = NOTE_BASE_FREQUENCIES[note_name] * (2 ** octave)
    
    return int(frequency)


# Parses the first line of a data file
def parse_metadata(metadata: list[str]) -> tuple[float, int, int]:
    # Metadata format as tempo, beat_count, beat_type
    tempo: float = float(metadata[0])
    beat_count: int = int(metadata[1])
    beat_type: int = int(metadata[2])

    return (tempo, beat_count, beat_type)


# Parse a single line of the data file that is not the first one
def parse_line(line: list, metadata: tuple) -> tuple[int, float]:
    note = line[0]

    tempo = metadata[0]
    beat_type = metadata[2]

    if note == "R":
        frequency = 0
    else:
        frequency = get_note_frequency(note)
    
    duration = get_note_duration(tempo, beat_type, int(line[2]), int(line[1]))
    
    print(frequency, duration)

    return (frequency, duration)


def parse_song(filename: str) -> list[tuple[int, float]]:
    """
    Parses an entire song data file and outputs it into a list of tuples which tell the buzzer what to do
    """
    buzzer_instructions = []

    print(filename)

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        metadata = parse_metadata(next(csvreader))
        
        for line in csvreader:
            note_data: tuple

            if line == []:
                continue
            else:
                note_data = parse_line(line, metadata)
                buzzer_instructions.append(note_data)

    return buzzer_instructions
