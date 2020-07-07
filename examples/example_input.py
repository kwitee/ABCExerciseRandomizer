from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.key import Key
from abc_exercise_randomizer.note_value import NoteValue
from abc_exercise_randomizer.note_length import NoteLength

note_distribution = [
    (NoteValue.a2, 4),
    (NoteValue.b2, 4),
    (NoteValue.c3, 3),
    (NoteValue.d3, 2),
    (NoteValue.e3, 1),
    (NoteValue.f3, 5),
    (NoteValue.g3, 3),
    (NoteValue.a3, 4),
    (NoteValue.b3, 4),
    (NoteValue.c4, 3),
    (NoteValue.d4, 2),
    (NoteValue.e4, 1),
    (NoteValue.f4, 5),
    (NoteValue.g4, 3),
    (NoteValue.rest, 2)
]

length_distribution = [
    (NoteLength.quarter, 6),
    (NoteLength.half, 4),
    (NoteLength.half_dot, 1),
    (NoteLength.whole, 1)
]

tie_probability = 0.05
syncopated = False
bar_length = BarLength.four
number_of_bars = 16
key = Key.F
