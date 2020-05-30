from typing import List, Tuple

from abc_exercise_randomizer.bar_generator import BarGenerator
from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.note_value import NoteValue
from abc_exercise_randomizer.note_length import NoteLength
from abc_exercise_randomizer.score_generator import ScoreGenerator


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
            bar_length: Defines how many quarter notes are in each bar (only meters with quarter notes are supported).
            number_of_bars: Number of bars to be generated (must be in <1;64>).
        """

        bar_generator = BarGenerator(note_distribution, length_distribution, tie_probability, bar_length)
        self.__score_generator = ScoreGenerator(bar_generator, bar_length, number_of_bars)

    def generate_exercise(self):
        """
        Generates random ABC exercise based on input parameters.

        Returns:
            Random ABC exercise in string form.
        """

        return self.__score_generator.generate_score()

    def generate_exercises(self, count: int):
        """
        Generates number of random ABC exercise based on input parameters.

        Parameters:
            count: Number of exercises. Can't be lower than one.
        Returns:
            Random ABC exercise in string form.
        """

        return self.__score_generator.generate_scores(count)
