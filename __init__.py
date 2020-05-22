from exercise_generator import ExerciseGenerator
from note_value import NoteValue
from note_length import NoteLength

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
    (NoteLength.quarter, 5),
    (NoteLength.half, 5),
    (NoteLength.half_dot, 1),
    (NoteLength.whole, 1)
]

tie_probability = 0.05

generator = ExerciseGenerator(note_distribution, length_distribution, tie_probability)
print(generator.generate_exercise())
