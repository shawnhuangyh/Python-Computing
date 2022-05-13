import random
import re
from typing import TextIO

from nltk.tokenize import sent_tokenize


class Markov:
    @staticmethod
    def __process_word(word: str):
        word = word.strip(r'"#$%&' r"'()*+-/:;<=>@[\]^_`{|}~")
        word = word.lstrip(r',.!?')
        if not word[:-1].replace("'", '').replace('-', '').isalpha() or (len(word) > 1 and word.isupper()):
            word = ''
        return word

    def __is_end_word(self, word: str):
        return word in self.end_words

    def __get_first_prefix(self):
        return list(random.choice(self.start_prefixes))

    def __get_next_word(self, prefix: tuple):
        seq = self.chain[prefix]
        return random.choice(seq)

    def __init__(self, fp: TextIO, n: int = 1):
        self.chain = {}
        self.start_prefixes_set = set()
        self.end_words = set()
        self.n = n
        fp.seek(0)
        text = ' '.join(line.strip() for line in fp)
        prefix = []
        for sentence in sent_tokenize(text):
            real_start = ''
            real_end = ''
            for word in re.split(r'\s', sentence):
                word = self.__process_word(word)
                if word != '':
                    if real_start == '':
                        if not word[0].isupper():
                            break
                        real_start = word
                    if len(prefix) == n:
                        key = tuple(prefix)
                        if prefix[0] == real_start:
                            self.start_prefixes_set.add(tuple(prefix))
                        if key in self.chain:
                            self.chain[key].append(word)
                        else:
                            self.chain[key] = [word]
                    prefix.append(word)
                    prefix = prefix[-n:]
                    real_end = word
            if real_end != '':
                if real_end[-1] in '.!?' and real_end.lower() not in ('mr.', 'mrs.'):
                    self.end_words.add(real_end)
        self.start_prefixes = list(self.start_prefixes_set)

    def __call__(self, n: int):
        while True:
            words = self.__get_first_prefix()
            pos = 0
            count = 0
            appeared_first_prefix = set()
            while True:
                try:
                    prefix = tuple(words[-self.n:])
                    word = self.__get_next_word(prefix)
                    words.append(word)
                    pos += 1
                    if pos == self.n:
                        if prefix in appeared_first_prefix:
                            words = words[:-self.n]
                            break
                        else:
                            appeared_first_prefix.add(prefix)
                    if word == '':
                        break
                    elif self.__is_end_word(word):
                        if count == n:
                            break
                        count += 1
                        pos = 0
                except KeyError:
                    break
            if not self.__is_end_word(words[-1]):
                continue
            return ' '.join(words)


def generate(m: int, n: int):
    with open('emma.txt') as f:
        markov = Markov(f, n)
    text = markov(m)
    print('\nm = {}, n = {}\n'.format(m, n))
    print(text)


if __name__ == '__main__':
    generate(10, 1)
    generate(10, 2)
    generate(10, 3)
