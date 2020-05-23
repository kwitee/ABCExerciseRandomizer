from typing import List

from abc_exercise_randomizer.bar import Bar


class Score:
    __LINE_BREAK = "!\n"
    __BAR_END = "|"
    __LAST_BAR_END = "|]"
    __LINE_BREAK_AFTER = 4

    def __init__(self, bars: List[Bar]):
        self.__bars = bars

    def get_bars(self):
        return self.__bars

    def __str__(self):
        score = str()

        for i, bar in enumerate(self.__bars):
            add_line_break = i != 0 and (i % self.__LINE_BREAK_AFTER == 0)
            bar_end = f"{self.__BAR_END if i != 0 else str()}{self.__LINE_BREAK if add_line_break else str()}"
            score = f"{score}{bar_end}{bar}"

        return f"{score}{self.__LAST_BAR_END}"
