from unittest.mock import Mock

import pytest

from abc_exercise_randomizer.score import Score


class TestScore:
    @pytest.mark.parametrize("bars, expected",
                             [
                                 (
                                     ["abcd", "efga"], "abcd|efga|]"
                                 ), (
                                     ["abcd", "efga", "ABCD", "EFGA", "abcd"], "abcd|efga|ABCD|EFGA|!\nabcd|]"
                                 )
                             ])
    def test_str(self, bars, expected):
        bar_mocks = []

        for bar in bars:
            bar_mock = Mock()
            bar_mock.__str__ = Mock()
            bar_mock.__str__.return_value = bar
            bar_mocks.append(bar_mock)

        score = Score(bar_mocks)
        assert str(score) == expected
