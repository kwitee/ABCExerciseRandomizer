import os
import random
from datetime import datetime

from bar import Bar
from note import Note
from score import Score


# TODO: better name in the header
# TODO: better input data
class ExerciseGenerator:
    __REST = "z"

    __bar_length = 4
    __possible_notes = ["c", "c", "B", "B", "d", "d", "e", "f", "g", __REST]
    __possible_lengths = [1, 1, 1, 1, 2, 2, 2, 3, 4]
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
            possible_length = [length for length in self.__possible_lengths if length <= remaining_length]
            note_length = random.choice(possible_length)
            note_value = random.choice(self.__get_possible_notes(length, previous_bar, note_value))

            length = length + note_length

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
            if last_note == self.__REST:
                possible_notes = [note for note in self.__possible_notes if note != self.__REST]

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
