from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.exercise_generator import ExerciseGenerator
from abc_exercise_randomizer.note_value import NoteValue
from abc_exercise_randomizer.note_length import NoteLength

note_distribution = [
    (NoteValue.c4, 1),
    (NoteValue.d4, 1),
    (NoteValue.e4, 1),
    (NoteValue.f4, 1),
    (NoteValue.g4, 1),
    (NoteValue.a3, 2),
    (NoteValue.b3, 2),
    (NoteValue.rest, 1)
]

length_distribution = [
    (NoteLength.eighth, 1),
    (NoteLength.quarter, 5),
    (NoteLength.half, 5),
    (NoteLength.half_dot, 1),
    (NoteLength.whole, 1)
]

tie_probability = 0.05
bar_length = BarLength.four
number_of_bars = 16

generator = ExerciseGenerator(note_distribution, length_distribution, tie_probability, bar_length, number_of_bars)
print(generator.generate_exercise())