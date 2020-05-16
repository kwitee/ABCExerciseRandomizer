import os
import random
from datetime import datetime

line_break = "!\n"
bar_end = "|"
last_bar_end = "|]"
tie = "-"
script_name = os.path.basename(__file__)
rest = "z"

exercise_name = f"Random exercise {datetime.now().strftime('%c')}"
default_note_length = "1/4"
tempo = "1/4 = 50"
meter = "C"
key = "C"

bar_length = 4
possible_notes = ["c", "c", "B", "B", "d", "d", "e", "f", "g", rest]
possible_lengths = [1, 1, 1, 1, 2, 2, 2, 3, 4]
line_break_after = 4
tie_probability = [True, False, False, False]

header = f"""X:1
T:{exercise_name}
M:{meter}
L:{default_note_length}
Q:{tempo}
K:{key}
I:abc-creator {script_name}"""

last_note = None


def generate_bar():
    current_length = 0
    bar = ""
    global last_note

    while current_length != bar_length:
        remaining_length = bar_length - current_length
        possible_new_length = [length for length in possible_lengths if length <= remaining_length]
        random_length = random.choice(possible_new_length)

        if last_note != rest:
            current_possible_notes = possible_notes
        else:
            current_possible_notes = [note for note in possible_notes if note != rest]

        last_note = random.choice(current_possible_notes)
        bar = f"{bar}{last_note}{random_length if random_length != 1 else str()}"
        current_length = current_length + random_length

    return bar


def generate_bars(number_of_bars):
    global last_note
    bars = ""

    for i in range(0, number_of_bars):
        add_line_break = i != 0 and (i % line_break_after == 0)
        current_bar_end = f"{bar_end if i != 0 else str()}{line_break if add_line_break else str()}"
        last_note_before_current = last_note
        current_bar = generate_bar()

        if current_bar[0] == last_note_before_current and random.choice(tie_probability):
            current_tie = tie
        else:
            current_tie = str()

        bars = f"{bars}{current_tie}{current_bar_end}{current_bar}"

    return f"{bars}{last_bar_end}"


print(header)
print(generate_bars(16))

# TODO: better name in the header
# TODO: better input data
# TODO: convert into classes and stop using globals
