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
        return f"{self.__value}{self.__length if self.__length > 1 else str()}{self.__TIE if self.__tie else str()}"
