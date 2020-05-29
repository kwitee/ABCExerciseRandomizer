import pytest

from abc_exercise_randomizer.bar import Bar
from abc_exercise_randomizer.bar_generator import BarGenerator
from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.note import Note
from abc_exercise_randomizer.note_length import NoteLength
from abc_exercise_randomizer.note_value import NoteValue


class TestBarGenerator:

    @pytest.mark.parametrize("note_distribution,length_distribution,tie_probability,bar_length,possible_tie,output",
                             [
                                 ([(NoteValue.rest, 1)], [(NoteLength.whole, 1)], 0, BarLength.four, False, "z4"),
                                 ([(NoteValue.b3, 1)], [(NoteLength.half, 1)], 0, BarLength.four, False, "B2B2"),
                                 ([(NoteValue.g4, 1)], [(NoteLength.quarter, 1)], 0, BarLength.four, False, "gggg"),
                                 ([(NoteValue.d4, 1)], [(NoteLength.quarter, 1)], 1, BarLength.four, False, "dddd"),
                                 ([(NoteValue.d4, 1)], [(NoteLength.quarter, 1)], 1, BarLength.four, True, "dddd-"),
                                 ([(NoteValue.d4, 1)], [(NoteLength.quarter, 1)], 0, BarLength.three, False, "ddd")
                             ])
    def test_generated_value(self, note_distribution, length_distribution, tie_probability, bar_length, possible_tie,
                             output):
        bar_generator = BarGenerator(note_distribution, length_distribution, tie_probability, bar_length)
        bar = bar_generator.generate_bar(possible_tie=possible_tie)
        assert str(bar) == output

    def test_post_tie_same_first_note(self):
        bar_generator = BarGenerator([(NoteValue.rest, 1)], [(NoteLength.whole, 1)], 0, BarLength.four)

        note_value = NoteValue.b3
        bar = bar_generator.generate_bar(Bar([Note(note_value, NoteLength.whole, True)]))

        assert bar.get_notes[0].get_value == note_value
