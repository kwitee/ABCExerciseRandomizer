from unittest.mock import Mock

import pytest

from abc_exercise_randomizer.bar import Bar


class TestNote:
    @pytest.mark.parametrize("notes, expected",
                             [
                                 (
                                     ["g", "d2-"], "gd2-"
                                 ), (
                                     ["A2", "B2"], "A2B2"
                                 ), (
                                     ["A4"], "A4"
                                 ), (
                                     ["c", "d", "e", "f-"], "cdef-"
                                 )
                             ])
    def test_str(self, notes, expected):
        note_mocks = []

        for note in notes:
            note_mock = Mock()
            note_mock.__str__ = Mock()
            note_mock.__str__.return_value = note
            note_mocks.append(note_mock)

        bar = Bar(note_mocks)
        assert str(bar) == expected
