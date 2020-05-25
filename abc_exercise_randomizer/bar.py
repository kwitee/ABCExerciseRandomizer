from typing import List

from abc_exercise_randomizer.note import Note


class Bar:
    def __init__(self, notes: List[Note]):
        self.__notes = notes

    @property
    def get_notes(self):
        return self.__notes

    def __str__(self):
        bar = str()

        for note in self.__notes:
            bar = bar + str(note)

        return bar
