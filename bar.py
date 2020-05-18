class Bar:
    def __init__(self, notes):
        self.__notes = notes

    def get_notes(self):
        return self.__notes

    def __str__(self):
        bar = str()

        for note in self.__notes:
            bar = bar + str(note)

        return bar
