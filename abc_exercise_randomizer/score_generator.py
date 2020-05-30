import os

from abc_exercise_randomizer.bar_generator import BarGenerator
from abc_exercise_randomizer.bar_length import BarLength
from abc_exercise_randomizer.score import Score


class ScoreGenerator:

    def __init__(self, bar_generator: BarGenerator, bar_length: BarLength, number_of_bars: int):
        """
        Creates score generator instance.

        Parameters:
            bar_generator: Bar generator used to generate score parts.
            bar_length: Defines how many quarter notes are in each bar (only meters with quarter notes are supported).
            number_of_bars: Number of bars to be generated (must be in <1;64>).
        """

        if number_of_bars < 1 or number_of_bars > 64:
            raise ValueError

        self.__bar_generator = bar_generator

        self.__meter = f"{BarLength(bar_length).value}/4"
        self.__score_name = f"Random score"
        self.__script_name = os.path.basename(__file__)
        self.__default_note_length = "1/4"
        self.__tempo = "1/4 = 50"
        self.__key = "C"
        self.__number_of_bars = number_of_bars

    def __generate_header(self, number: int):
        if number < 1:
            raise ValueError

        return f"X:{number}\n" \
               f"T:{number} - {self.__score_name}\n" \
               f"M:{self.__meter}\n" \
               f"L:{self.__default_note_length}\n" \
               f"Q:{self.__tempo}\n" \
               f"K:{self.__key}\n" \
               f"I:abc-creator {self.__script_name}\n"

    def __generate_body(self):
        bars = []
        bar = None

        for i in range(0, self.__number_of_bars):
            possible_tie = i != self.__number_of_bars - 1
            bar = self.__bar_generator.generate_bar(bar, possible_tie)
            bars.append(bar)

        return Score(bars)

    def generate_score(self):
        """
        Generates random score based on input parameters.

        Returns:
            Random score in string form.
        """

        return self.__generate_score_with_number()

    def __generate_score_with_number(self, number: int = 1):
        return f"{self.__generate_header(number)}{self.__generate_body()}"

    __SCORE_DELIMITER = "\n\n"

    def generate_scores(self, count: int):
        """
        Generates number of random scores based on input parameters.

        Parameters:
            count: Number of scores. Can't be lower than one.
        Returns:
            Random score in string form.
        """

        if count < 1:
            raise ValueError

        scores = str()

        for number in range(count):
            delimiter = str() if number == 0 else self.__SCORE_DELIMITER
            scores = scores + delimiter + self.__generate_score_with_number(number + 1)

        return scores
