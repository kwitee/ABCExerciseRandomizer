import sys

from abc_exercise_randomizer.exercise_generator import ExerciseGenerator
from examples.example_input import *


file_name = sys.argv[1]
generator = ExerciseGenerator(note_distribution, length_distribution, tie_probability, syncopated, bar_length,
                              number_of_bars)

with open(file_name, "w") as file:
    file.write(generator.generate_exercises(20))
