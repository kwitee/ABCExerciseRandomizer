import os
import random
from datetime import datetime
from typing import List, Tuple

from abc_exercise_randomizer.bar import Bar
from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.note import Note
from abc_exercise_randomizer.score import Score
from abc_exercise_randomizer.note_value import NoteValue
from abc_exercise_randomizer.note_length import NoteLength


class ExerciseGenerator:

    def __init__(self, note_distribution: List[Tuple[NoteValue, int]],
                 length_distribution: List[Tuple[NoteLength, int]],
                 tie_probability: float, bar_length: BarLength, number_of_bars: int):
        """
        Creates exercise generator instance.

        Parameters:
            note_distribution: Note probability distribution, higher value means greater probability.
            length_distribution: Length probability distribution, higher value means greater probability.
            tie_probability: Probability of ties between bars (must be in <0;1>).
            bar_length: Defines how many quarter notes is in each bar (meters not based on quarter notes are not supported).
            number_of_bars: Number of bars to be generated (must be in <1;64>).
        """

        if tie_probability < 0 or tie_probability > 1:
            raise ValueError
        if number_of_bars < 1 or number_of_bars > 64:
            raise ValueError

        self.__possible_notes = self.__unroll_distribution(note_distribution)
        self.__possible_lengths = self.__unroll_distribution(length_distribution)
        self.__tie_probability = tie_probability
        self.__bar_length = BarLength(bar_length).value

        self.__meter = f"{self.__bar_length}/4"
        self.__exercise_name = f"Random exercise {datetime.now().strftime('%c')}"
        self.__script_name = os.path.basename(__file__)
        self.__default_note_length = "1/4"
        self.__tempo = "1/4 = 50"
        self.__key = "C"
        self.__number_of_bars = number_of_bars

    @staticmethod
    def __unroll_distribution(distribution):
        output = []

        for weight in distribution:
            for _ in range(weight[1]):
                output.append(weight[0])

        return output

    def __generate_header(self):
        return f"X:1\n" \
               f"T:{self.__exercise_name}\n" \
               f"M:{self.__meter}\n" \
               f"L:{self.__default_note_length}\n" \
               f"Q:{self.__tempo}\n" \
               f"K:{self.__key}\n" \
               f"I:abc-creator {self.__script_name}\n"

    def __generate_bar(self, previous_bar: Bar, last_bar: bool):
        length = 0
        notes = []
        note_value = str()

        while length != self.__bar_length:
            remaining_length = self.__bar_length - length
            possible_length = [length for length in self.__possible_lengths if length.value <= remaining_length]
            note_length = random.choice(possible_length)
            note_value = random.choice(self.__get_possible_notes(length, previous_bar, note_value))

            length = length + note_length.value

            tie = not last_bar and length == self.__bar_length and self.__tie_probability > random.random()
            notes.append(Note(note_value, note_length, tie))

        return Bar(notes)

    def __get_possible_notes(self, length: int, previous_bar: Bar, last_note: NoteValue):
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
        """
        Generates random ABC exercise based on input parameters.

        Returns:
            Random ABC exercise in string form.
        """

        return f"{self.__generate_header()}{self.__generate_score()}"
