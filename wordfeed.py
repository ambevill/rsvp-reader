from settings import STOPS, WPM

# This class generates words/phrases to display and the length of time in
# milliseconds to display each (based on words/minute and pauses for stops.)
class WordFeed(object):
    def __init__(self, text, inext=0):
        self.text_tuple = tuple(text.split())
        self.inext = inext if inext <= len(self.text_tuple) else 0
        self.wpm_delay_ms = int(60000 / WPM)

    def next(self):
        self.inext = max(self.inext, 0)
        if len(self.text_tuple) <= self.inext:
            return None, None
        text = self.text_tuple[self.inext]
        self.inext += 1
        delay_ms = self.calculate_delay_ms(text)
        return text, delay_ms

    def calculate_delay_ms(self, text):
        stop_delay = 0
        for stop, word_frac in STOPS.iteritems():
            if stop in text:
                stop_delay = max(stop_delay, word_frac * self.wpm_delay_ms)
        return self.wpm_delay_ms + int(stop_delay)
