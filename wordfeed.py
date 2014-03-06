from settings import STOPS, WPM
from freq_dict import FREQ_DICT

# This class generates words/phrases to display and the length of time in
# milliseconds to display each (based on words/minute and pauses for stops.)
class WordFeed(object):
    def __init__(self, text, inext=0):
        self.text_tuple = tuple(text.split())
        self.inext = inext if inext <= len(self.text_tuple) else 0
        self.wpm_delay_ms = int(60000 / WPM)
        self.delay_tuple = None
        self.preprocess_delays()

    def preprocess_delays(self):
        delays = []
        for text in self.text_tuple:
            delay = self.calculate_delay_ms(text)
            delays.append(delay)
        self.delay_tuple = tuple(delays)

    def calculate_delay_ms(self, text):
        stop_delay = int(STOPS.get(text[-1], 0) * self.wpm_delay_ms)
        freq_delay = int(FREQ_DICT.get_delay_words(text) * self.wpm_delay_ms)
        return self.wpm_delay_ms + stop_delay + freq_delay

    def next(self):
        self.inext = max(self.inext, 0)
        if len(self.text_tuple) <= self.inext:
            return None, None
        text = self.text_tuple[self.inext]
        self.inext += 1
        delay_ms = self.calculate_delay_ms(text)
        return text, delay_ms
