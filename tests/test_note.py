import pytest

from abc_exercise_randomizer.note import Note
from abc_exercise_randomizer.note_length import NoteLength
from abc_exercise_randomizer.note_value import NoteValue


class TestNote:
    @pytest.mark.parametrize("note_value,note_length,tie,expected", [(NoteValue.a3, NoteLength.quarter, True, "A-"),
                                                                     (NoteValue.c4, NoteLength.half, False, "c2"),
                                                                     (NoteValue.d4, NoteLength.whole, True, "d4-"),
                                                                     (NoteValue.g4, NoteLength.half_dot, False, "g3")])
    def test_str(self, note_value, note_length, tie, expected):
        note = Note(note_value, note_length, tie)
        assert str(note) == expected
