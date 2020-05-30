import random
from typing import List, Tuple

from abc_exercise_randomizer.bar import Bar
from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.note import Note
from abc_exercise_randomizer.note_length import NoteLength
from abc_exercise_randomizer.note_value import NoteValue


class BarGenerator:
    def __init__(self, note_distribution: List[Tuple[NoteValue, int]],
                 length_distribution: List[Tuple[NoteLength, int]],
                 tie_probability: float, bar_length: BarLength):
        """
        Creates bar generator instance.

        Parameters:
            note_distribution: Note probability distribution, higher value means greater probability.
            length_distribution: Length probability distribution, higher value means greater probability.
            tie_probability: Probability of ties between bars (must be in <0;1>).
            bar_length: Defines how many quarter notes are in each bar (only meters with quarter notes are supported).
        """

        if tie_probability < 0 or tie_probability > 1:
            raise ValueError

        self.__possible_notes = self.__unroll_distribution(note_distribution)
        self.__possible_lengths = self.__unroll_distribution(length_distribution)
        self.__tie_probability = tie_probability
        self.__bar_length = BarLength(bar_length).value

    @staticmethod
    def __unroll_distribution(distribution):
        output = []

        for weight in distribution:
            for _ in range(weight[1]):
                output.append(weight[0])

        return output

    def generate_bar(self, previous_bar: Bar = None, possible_tie: bool = False):
        """
        Generates random bar based on input parameters.

        Parameters:
            previous_bar: previously generated bar, None if this is the first bar.
            possible_tie: controls if the ban can have a tie at the end.
        Returns:
            Random ABC exercise in string form.
        """

        length = 0
        notes = []
        note_value = str()

        while length < self.__bar_length:
            note_length = random.choice(self.__get_possible_lengths(length))
            note_value = random.choice(self.__get_possible_notes(length, previous_bar, note_value))

            length = length + note_length.value.value

            tie = possible_tie and length == self.__bar_length and self.__tie_probability > random.random()
            notes.append(Note(note_value, note_length, tie))

        return Bar(notes)

    def __get_possible_lengths(self, length):
        remaining_length = self.__bar_length - length
        return [length for length in self.__possible_lengths if length.value.value <= remaining_length]

    def __get_possible_notes(self, length: int, previous_bar: Bar, last_note: NoteValue):
        possible_notes = self.__possible_notes

        if length == 0 and previous_bar is not None:
            last_note_in_previous_bar = previous_bar.get_notes[-1]

            if last_note_in_previous_bar.get_tie:
                possible_notes = [last_note_in_previous_bar.get_value]
        else:
            if last_note == NoteValue.rest:
                possible_notes = [note for note in self.__possible_notes if note != NoteValue.rest]

        return possible_notes
