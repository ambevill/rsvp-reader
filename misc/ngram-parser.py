# Use Google 1grams to calculate the N most-frequently used words and
# their frequency of use since 2004.
# Visit http://storage.googleapis.com/books/ngrams/books/datasetsv2.html for
# raw data to parse

N = 100000
min_year, max_year = 2005, 2009
attribution = '''# {0} most frequently used 1-grams in American English \
books, {1}--{2}. Data condensed from Google Ngrams Version 2, Copyright \
2012, at <http://storage.googleapis.com/books/ngrams/books/datasetsv2.html>.\
'''.format(N, min_year, max_year)
ngram_path_base = '~/path/to/googlebooks-eng-us-all-1gram-20120701-{0}'
output_path = '../frequent-words.csv'

import numpy as np
import os

ngram_paths = \
    [ngram_path_base.format(v) for v in '0123456789abcdefghijklmnopqrstuvwxyz'] + \
    [ngram_path_base.format('other')]

previous_word = None

class Parser(object):
    def __init__(self, N):
        self.N = N
        self.phrases = N * ['']
        self.frequencies = np.zeros(N, dtype='int64')
        self.imin = 0
        self.min_freq = 0

    def update_list(self, new_phrase, new_freq):
        self.phrases[self.imin] = new_phrase
        self.frequencies[self.imin] = new_freq
        self.imin = self.frequencies.argmin()
        self.min_freq = self.frequencies[self.imin]

    def evaluate_file(self, pipe):
        phrase = ''
        frequency = 0
        for iline,line in enumerate(pipe):
            if iline % 1000000 == 0:
                print '... {0} million...'.format(iline / 1000000)
            split = line.split('\t')
            if not min_year <= int(split[1]) <= max_year:
                continue
            if split[0][-4:] in ('_DET', '_ADP', '_PRT', '_ADV', '_NUM', '_ADJ'):
                continue
            if split[0][-5:] in ('_CONJ', '_PRON', '_VERB', '_NOUN'):
                continue
            if split[0] != phrase:
                if frequency > self.min_freq:
                    self.update_list(phrase, frequency)
                phrase = split[0]
                frequency = 0
            frequency += int(split[2])
        if frequency > self.min_freq:
            self.update_list(phrase, frequency)

    def evaluate_paths(self, ngram_paths):
        for path in ngram_paths:
            print path
            with open(os.path.expanduser(path)) as pipe:
                self.evaluate_file(pipe)

    def export_results(self, path):
        cmp_zipped = lambda v1,v2: -cmp(v1[1], v2[1])
        pairs = zip(self.phrases, self.frequencies)
        pairs.sort(cmp_zipped)
        print 'Writing {0} values to {1}'.format(N, output_path)
        with open(output_path, 'w') as pipe:
            pipe.write('{0}\n'.format(attribution))
            for pair in pairs:
                pipe.write('{0}\t{1}\n'.format(*pair))


parser = Parser(N)
parser.evaluate_paths(ngram_paths)
parser.export_results(output_path)
