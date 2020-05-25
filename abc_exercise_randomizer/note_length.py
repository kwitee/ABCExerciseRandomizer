from enum import Enum
from collections import namedtuple

NoteLengthDefinition = namedtuple('NoteLengthDefinition', ['value', 'display_string'])


class NoteLength(Enum):

    @property
    def display_string(self):
        return self.value.display_string

    eighth = NoteLengthDefinition(0.5, "/2")
    quarter = NoteLengthDefinition(1, str())
    half = NoteLengthDefinition(2, "2")
    half_dot = NoteLengthDefinition(3, "3")
    whole = NoteLengthDefinition(4, "4")
