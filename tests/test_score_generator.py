from unittest.mock import Mock

import pytest

from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.key import Key
from abc_exercise_randomizer.score_generator import ScoreGenerator


class TestScoreGenerator:

    @staticmethod
    def __create_bar_generator_mock():
        bar_generator_mock = Mock()
        bar_mock = Mock()
        bar_generator_mock.generate_bar.return_value = bar_mock
        bar_mock.__str__ = Mock()
        bar_mock.__str__.return_value = "BAR"
        return bar_generator_mock

    @pytest.mark.parametrize("bar_length,number_of_bars,key,output",
                             [
                                 (BarLength.four, 1, Key.C, "X:1\n"
                                                            "T:1 - Random score\n"
                                                            "M:4/4\n"
                                                            "L:1/4\n"
                                                            "Q:1/4 = 50\n"
                                                            "K:C\n"
                                                            "I:abc-creator score_generator.py\n"
                                                            "BAR|]"),
                                 (BarLength.three, 4, Key.G, "X:1\n"
                                                             "T:1 - Random score\n"
                                                             "M:3/4\n"
                                                             "L:1/4\n"
                                                             "Q:1/4 = 50\n"
                                                             "K:G\n"
                                                             "I:abc-creator score_generator.py\n"
                                                             "BAR|BAR|BAR|BAR|]")
                             ])
    def test_generate_score(self, bar_length, number_of_bars, key, output):
        score_generator = ScoreGenerator(self.__create_bar_generator_mock(), bar_length, number_of_bars, key)
        assert score_generator.generate_score() == output

    @pytest.mark.parametrize("bar_length,number_of_bars,number_of_scores,key,output",
                             [
                                 (BarLength.four, 3, 1, Key.C, "X:1\n"
                                                               "T:1 - Random score\n"
                                                               "M:4/4\n"
                                                               "L:1/4\n"
                                                               "Q:1/4 = 50\n"
                                                               "K:C\n"
                                                               "I:abc-creator score_generator.py\n"
                                                               "BAR|BAR|BAR|]"),
                                 (BarLength.two, 2, 2, Key.G, "X:1\n"
                                                              "T:1 - Random score\n"
                                                              "M:2/4\n"
                                                              "L:1/4\n"
                                                              "Q:1/4 = 50\n"
                                                              "K:G\n"
                                                              "I:abc-creator score_generator.py\n"
                                                              "BAR|BAR|]\n"
                                                              "\n"
                                                              "X:2\n"
                                                              "T:2 - Random score\n"
                                                              "M:2/4\n"
                                                              "L:1/4\n"
                                                              "Q:1/4 = 50\n"
                                                              "K:G\n"
                                                              "I:abc-creator score_generator.py\n"
                                                              "BAR|BAR|]"),
                             ])
    def test_generate_scores(self, bar_length, number_of_bars, number_of_scores, key, output):
        score_generator = ScoreGenerator(self.__create_bar_generator_mock(), bar_length, number_of_bars, key)
        assert score_generator.generate_scores(number_of_scores) == output
