import os
import random
from datetime import datetime

from bar import Bar
from note import Note
from score import Score
from note_value import NoteValue


# TODO: better name in the header
# TODO: add tie probability as an input, in format 0.1
# TODO: meter input (3/4 etc.)
class ExerciseGenerator:
    __possible_notes = []
    __possible_lengths = []

    def __init__(self, note_distribution, length_distribution):
        for note_weight in note_distribution:
            for _ in range(note_weight[1]):
                self.__possible_notes.append(note_weight[0])

        for length_weight in length_distribution:
            for _ in range(length_weight[1]):
                self.__possible_lengths.append(length_weight[0])

    __bar_length = 4
    __tie_probability = [True, False, False, False, False, False, False, False]

    __exercise_name = f"Random exercise {datetime.now().strftime('%c')}"
    __script_name = os.path.basename(__file__)
    __default_note_length = "1/4"
    __tempo = "1/4 = 50"
    __meter = "C"
    __key = "C"
    __number_of_bars = 16

    def __generate_header(self):
        return f"X:1\n" \
               f"T:{self.__exercise_name}\n" \
               f"M:{self.__meter}\n" \
               f"L:{self.__default_note_length}\n" \
               f"Q:{self.__tempo}\n" \
               f"K:{self.__key}\n" \
               f"I:abc-creator {self.__script_name}\n"

    def __generate_bar(self, previous_bar, last_bar):
        length = 0
        notes = []
        note_value = str()

        while length != self.__bar_length:
            remaining_length = self.__bar_length - length
            possible_length = [length for length in self.__possible_lengths if length.value <= remaining_length]
            note_length = random.choice(possible_length)
            note_value = random.choice(self.__get_possible_notes(length, previous_bar, note_value))

            length = length + note_length.value

            tie = not last_bar and length == self.__bar_length and random.choice(self.__tie_probability)
            notes.append(Note(note_value, note_length, tie))

        return Bar(notes)

    def __get_possible_notes(self, length, previous_bar, last_note):
        possible_notes = self.__possible_notes

        if length == 0 and previous_bar is not None:
            last_note_in_previous_bar = previous_bar.get_notes()[-1]

            if last_note_in_previous_bar.get_tie():
                possible_notes = [note for note in self.__possible_notes
                                  if note == last_note_in_previous_bar.get_value()]
        else:
            if last_note == NoteValue.rest:
                possible_notes = [note for note in self.__possible_notes if note != NoteValue.rest]

        return possible_notes

    def __generate_score(self):
        bars = []
        bar = None

        for i in range(0, self.__number_of_bars):
            bar = self.__generate_bar(bar, i == self.__number_of_bars - 1)
            bars.append(bar)

        return Score(bars)

    def generate_exercise(self):
        return f"{self.__generate_header()}{self.__generate_score()}"
