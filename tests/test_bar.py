import pytest

from abc_exercise_randomizer.bar import Bar
from abc_exercise_randomizer.note import Note
from abc_exercise_randomizer.note_length import NoteLength
from abc_exercise_randomizer.note_value import NoteValue


class TestNote:
    @pytest.mark.parametrize("notes, expected",
                             [
                                 (
                                     [
                                         Note(NoteValue.g4, NoteLength.quarter, False),
                                         Note(NoteValue.d4, NoteLength.half, True)
                                     ], "gd2-"
                                 ), (
                                     [
                                         Note(NoteValue.a3, NoteLength.half, False),
                                         Note(NoteValue.b3, NoteLength.half, False)
                                     ], "A2B2"
                                 ), (
                                     [
                                         Note(NoteValue.a3, NoteLength.whole, False)
                                     ], "A4"
                                 ), (
                                     [
                                         Note(NoteValue.c4, NoteLength.quarter, False),
                                         Note(NoteValue.d4, NoteLength.quarter, False),
                                         Note(NoteValue.e4, NoteLength.quarter, False),
                                         Note(NoteValue.f4, NoteLength.quarter, True)
                                     ], "cdef-"
                                 )
                             ])
    def test_str(self, notes, expected):
        bar = Bar(notes)
        assert str(bar) == expected
