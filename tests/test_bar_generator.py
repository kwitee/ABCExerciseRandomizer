from unittest.mock import patch

import pytest

from abc_exercise_randomizer.bar import Bar
from abc_exercise_randomizer.bar_generator import BarGenerator
from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.note import Note
from abc_exercise_randomizer.note_length import NoteLength
from abc_exercise_randomizer.note_value import NoteValue


class TestBarGenerator:

    @pytest.mark.parametrize("note_distribution,length_distribution,tie_probability,"
                             "bar_length,possible_tie,syncopated,output",
                             [
                                 ([(NoteValue.rest, 1)], [(NoteLength.whole, 1)], 0, BarLength.four,
                                  False, True, "z4"),
                                 ([(NoteValue.b3, 1)], [(NoteLength.half, 1)], 0, BarLength.four,
                                  False, True, "B2B2"),
                                 ([(NoteValue.g4, 1)], [(NoteLength.quarter, 1)], 0, BarLength.four,
                                  False, True, "gggg"),
                                 ([(NoteValue.d4, 1)], [(NoteLength.quarter, 1)], 1, BarLength.four,
                                  False, True, "dddd"),
                                 ([(NoteValue.d4, 1)], [(NoteLength.quarter, 1)], 1, BarLength.four,
                                  True, True, "dddd-"),
                                 ([(NoteValue.d4, 1)], [(NoteLength.quarter, 1)], 0, BarLength.three,
                                  False, True, "ddd")
                             ])
    def test_generate_bar(self, note_distribution, length_distribution, tie_probability, bar_length, possible_tie,
                          syncopated, output):
        bar_generator = BarGenerator(note_distribution, length_distribution, tie_probability, syncopated, bar_length)
        bar = bar_generator.generate_bar(possible_tie=possible_tie)
        assert str(bar) == output

    def test_generate_bar_post_tie_same_first_note(self):
        bar_generator = BarGenerator([(NoteValue.rest, 1)], [(NoteLength.whole, 1)], 0, True, BarLength.four)

        note_value = NoteValue.b3
        bar = bar_generator.generate_bar(Bar([Note(note_value, NoteLength.whole, True)]))

        assert bar.get_notes[0].get_value == note_value

    def test_generate_bar_not_syncopated(self):
        bar_generator = BarGenerator([(NoteValue.d4, 1)], [(NoteLength.quarter, 1), (NoteLength.eighth, 1)],
                                     0, False, BarLength.four)
        first_random_value = True

        def random_choice(seq):
            nonlocal first_random_value
            index = 1 if first_random_value else 0
            first_random_value = False
            return seq[index]

        with patch('random.choice', side_effect=lambda seq: random_choice(seq)) as _:
            assert str(bar_generator.generate_bar()) == "d/2d/2ddd"
