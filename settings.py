import tkFont

# How many words per minute.
WPM = 300

# Font to display RSVP text
RSVP_FONT_DICT = {
    'family': 'Helvetica',
    'size': 36,
}

# How many word-lengths to pause if the displayed text contains punctuation
# For example, pause for an additional word-length when a period is displayed.
STOPS = {
    '.': 1,
    ',': 0.5,
    ';': 0.8,
}

# Dimensions of the RSVP display box in pixels (width, height)
RSVP_SHAPE = (600, 100)
