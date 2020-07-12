from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.exercise_generator_input import ExerciseGeneratorInput
from abc_exercise_randomizer.key import Key
from abc_exercise_randomizer.note_value import NoteValue
from abc_exercise_randomizer.note_length import NoteLength


class ExerciseGeneratorInputs:
    @property
    def c_key_input(self):
        exercise_input = ExerciseGeneratorInput()

        exercise_input.note_distribution = [
            (NoteValue.a2, 2),
            (NoteValue.b2, 1),
            (NoteValue.c3, 5),
            (NoteValue.d3, 3),
            (NoteValue.e3, 4),
            (NoteValue.f3, 4),
            (NoteValue.g3, 3),
            (NoteValue.a3, 2),
            (NoteValue.b3, 1),
            (NoteValue.c4, 5),
            (NoteValue.d4, 3),
            (NoteValue.e4, 4),
            (NoteValue.f4, 4),
            (NoteValue.g4, 3),
            (NoteValue.rest, 2)
        ]

        exercise_input.length_distribution = [
            (NoteLength.quarter, 6),
            (NoteLength.half, 1)
        ]

        exercise_input.tie_probability = 0.05
        exercise_input.syncopated = False
        exercise_input.bar_length = BarLength.two
        exercise_input.number_of_bars = 16
        exercise_input.key = Key.C

        return exercise_input

    @property
    def g_key_input(self):
        exercise_input = ExerciseGeneratorInput()

        exercise_input.note_distribution = [
            (NoteValue.a2, 3),
            (NoteValue.b2, 4),
            (NoteValue.c3, 4),
            (NoteValue.d3, 3),
            (NoteValue.e3, 1),
            (NoteValue.f3, 3),
            (NoteValue.g3, 5),
            (NoteValue.a3, 3),
            (NoteValue.b3, 4),
            (NoteValue.c4, 4),
            (NoteValue.d4, 3),
            (NoteValue.e4, 1),
            (NoteValue.f4, 3),
            (NoteValue.g4, 5),
            (NoteValue.rest, 2)
        ]

        exercise_input.length_distribution = [
            (NoteLength.quarter, 6),
            (NoteLength.half, 4),
            (NoteLength.half_dot, 1)
        ]

        exercise_input.tie_probability = 0.05
        exercise_input.syncopated = False
        exercise_input.bar_length = BarLength.three
        exercise_input.number_of_bars = 16
        exercise_input.key = Key.G

        return exercise_input

    @property
    def f_key_input(self):
        exercise_input = ExerciseGeneratorInput()

        exercise_input.note_distribution = [
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

        exercise_input.length_distribution = [
            (NoteLength.quarter, 6),
            (NoteLength.half, 4),
            (NoteLength.half_dot, 1),
            (NoteLength.whole, 1)
        ]

        exercise_input.tie_probability = 0.05
        exercise_input.syncopated = False
        exercise_input.bar_length = BarLength.four
        exercise_input.number_of_bars = 16
        exercise_input.key = Key.F

        return exercise_input
