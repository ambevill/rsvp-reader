import math

# How many words per minute.
WPM = 300

# Font to display RSVP text
RSVP_FONT_DICT = {
    'family': 'Helvetica',
    'size': 36,
}

# How many word-lengths to pause if the displayed text ends with punctuation.
# For example, pause for an additional word-length when a period is displayed.
STOPS = {
    '.': 1,
    '?': 1,
    '!': 1,
    ',': 0.5,
    ';': 0.8,
}

# Dimensions of the RSVP display box in pixels (width, height)
RSVP_SHAPE = (600, 100)

# How many additional word-lengths to hesitate as a function of the word
# frequency. The rank is the position of the word in the sorted frequency
# data. For example, "the" has frequency 3433135677 and rank 0. The
# minimum and maximum of the frequency data are
# passed in as min_freq and max_freq.
def FREQUENCY_DELAY(freq, rank, min_freq, max_freq):
    if rank < 2000:
        return 0
    if rank < 5000:
        return 0.33
    if rank < 20000:
        return 0.66
    if rank < 100000:
        return 1
    return 1.33
