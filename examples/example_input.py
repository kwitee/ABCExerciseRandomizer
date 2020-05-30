from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.note_value import NoteValue
from abc_exercise_randomizer.note_length import NoteLength

note_distribution = [
    (NoteValue.g3, 3),
    (NoteValue.a3, 2),
    (NoteValue.b3, 2),
    (NoteValue.c4, 1),
    (NoteValue.d4, 1),
    (NoteValue.e4, 1),
    (NoteValue.f4, 1),
    (NoteValue.g4, 1),
    (NoteValue.rest, 1)
]

length_distribution = [
    (NoteLength.eighth, 1),
    (NoteLength.quarter, 6),
    (NoteLength.half, 4),
    (NoteLength.half_dot, 1),
    (NoteLength.whole, 1)
]

tie_probability = 0.05
syncopated = False
bar_length = BarLength.four
number_of_bars = 16
