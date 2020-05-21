from note_length import NoteLength
from note_value import NoteValue


class Note:
    __TIE = "-"

    def __init__(self, value, length, tie):
        self.__value = value
        self.__length = length
        self.__tie = tie

    def get_value(self):
        return self.__value

    def get_length(self):
        return self.__length

    def get_tie(self):
        return self.__tie

    def __str__(self):
        value = NoteValue(self.__value).value
        length = NoteLength(self.__length).value if self.__length != NoteLength.quarter else str()
        tie = self.__TIE if self.__tie else str()
        return f"{value}{length}{tie}"
