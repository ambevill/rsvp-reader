from settings import FREQUENCY_DELAY
from os.path import dirname, join

# This class loads a 'dictionary' of frequently used words and their frequency
# and returns the corresponding delay length (in milliseconds) upon request
class FrequencyDict(object):
    def __init__(self, csv_path):
        self.fd = {}
        with open(csv_path) as csv_file:
            rank = 0
            for line in csv_file:
                if '\t' not in line:
                    continue
                rank += 1
                split = line.split('\t')
                word = split[0]
                freq = int(split[1])
                self.fd[word] = (freq, rank)
        self.min_freq = min(self.fd.itervalues())
        self.max_freq = max(self.fd.itervalues())

    def get_delay_words(self, text):
        freq, rank = self.fd.get(text, (0, len(self.fd)))
        return FREQUENCY_DELAY(freq, rank, self.min_freq, self.max_freq)

try:
    from __main__ import __file__ as main_path
except ImportError:
    main_path = None
    csv_path = None
    FREQ_DICT = None
else:
    csv_path = join(dirname(main_path), 'frequent-words.csv')
    FREQ_DICT = FrequencyDict(csv_path)

if __name__ == '__main__':
    FREQ_DICT = FrequencyDict('frequent-words.csv')
