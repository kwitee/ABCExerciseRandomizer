import sys

from abc_exercise_randomizer.exercise_generator import ExerciseGenerator
from abc_exercise_randomizer.exercise_generator_inputs import ExerciseGeneratorInputs


def main(file_name):
    generator = ExerciseGenerator(ExerciseGeneratorInputs().g_key_input)

    with open(file_name, "w") as file:
        file.write(generator.generate_exercises(20))


if __name__ == "__main__":
    main(sys.argv[1])
