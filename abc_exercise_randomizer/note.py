from abc_exercise_randomizer.note_length import NoteLength
from abc_exercise_randomizer.note_value import NoteValue


class Note:
    __TIE = "-"

    def __init__(self, value: NoteValue, length: NoteLength, tie: bool):
        self.__value = value
        self.__length = length
        self.__tie = tie

    @property
    def get_value(self):
        return self.__value

    @property
    def get_length(self):
        return self.__length

    @property
    def get_tie(self):
        return self.__tie

    def __str__(self):
        value = NoteValue(self.__value).value
        length = NoteLength(self.__length).display_string
        tie = self.__TIE if self.__tie else str()
        return f"{value}{length}{tie}"
