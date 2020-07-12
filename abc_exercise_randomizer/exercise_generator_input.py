from typing import List, Tuple

from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.key import Key
from abc_exercise_randomizer.note_value import NoteValue
from abc_exercise_randomizer.note_length import NoteLength


class ExerciseGeneratorInput:
    def __init__(self, note_distribution: List[Tuple[NoteValue, int]] = None,
                 length_distribution: List[Tuple[NoteLength, int]] = None,
                 tie_probability: float = None, syncopated: bool = None, bar_length: BarLength = None,
                 number_of_bars: int = None, key: Key = None):
        """
        Creates exercise generator input instance.

        Parameters:
            note_distribution: Note probability distribution, higher value means greater probability.
            length_distribution: Length probability distribution, higher value means greater probability.
            tie_probability: Probability of ties between bars (must be in <0;1>).
            syncopated: Defines if the rhythm can be syncopated.
            bar_length: Defines how many quarter notes are in each bar (only meters with quarter notes are supported).
            number_of_bars: Number of bars to be generated (must be in <1;64>).
        """

        self.__note_distribution = note_distribution
        self.__length_distribution = length_distribution
        self.__tie_probability = tie_probability
        self.__syncopated = syncopated
        self.__bar_length = bar_length
        self.__number_of_bars = number_of_bars
        self.__key = key

    @property
    def note_distribution(self):
        return self.__note_distribution

    @note_distribution.setter
    def note_distribution(self, value: List[Tuple[NoteValue, int]]):
        self.__note_distribution = value

    @property
    def length_distribution(self):
        return self.__length_distribution

    @length_distribution.setter
    def length_distribution(self, value: List[Tuple[NoteLength, int]]):
        self.__length_distribution = value

    @property
    def tie_probability(self):
        return self.__tie_probability

    @tie_probability.setter
    def tie_probability(self, value: float):
        self.__tie_probability = value

    @property
    def syncopated(self):
        return self.__syncopated

    @syncopated.setter
    def syncopated(self, value: bool):
        self.__syncopated = value

    @property
    def bar_length(self):
        return self.__bar_length

    @bar_length.setter
    def bar_length(self, value: BarLength):
        self.__bar_length = value

    @property
    def number_of_bars(self):
        return self.__number_of_bars

    @number_of_bars.setter
    def number_of_bars(self, value: int):
        self.__number_of_bars = value

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value: Key):
        self.__key = value
