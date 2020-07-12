from abc_exercise_randomizer.exercise_generator import ExerciseGenerator
from abc_exercise_randomizer.exercise_generator_inputs import ExerciseGeneratorInputs


def main():
    generator = ExerciseGenerator(ExerciseGeneratorInputs().g_key_input)
    print(generator.generate_exercise())


if __name__ == "__main__":
    main()
