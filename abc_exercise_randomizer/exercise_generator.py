from abc_exercise_randomizer.bar_generator import BarGenerator
from abc_exercise_randomizer.exercise_generator_input import ExerciseGeneratorInput
from abc_exercise_randomizer.score_generator import ScoreGenerator


class ExerciseGenerator:

    def __init__(self, input_data: ExerciseGeneratorInput):
        """
        Creates exercise generator instance.

        Parameters:
            input_data: Object with exercise generator input values.
        """

        bar_generator = BarGenerator(input_data.note_distribution, input_data.length_distribution,
                                     input_data.tie_probability, input_data.syncopated, input_data.bar_length)
        self.__score_generator = ScoreGenerator(bar_generator, input_data.bar_length, input_data.number_of_bars,
                                                input_data.key)

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
