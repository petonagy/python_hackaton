from typing import Set
from unidecode import unidecode


class StopWords(object):
    def __init__(self):
        self._words = set()
        self._decoded_words = set()
        self._load()

    @property
    def words(self) -> Set[str]:
        return self._words

    def decoded_words(self) -> Set[str]:
        return self._decoded_words

    def _load(self):
        with open('../resources/stopwords1.txt', 'r', encoding='utf8') as f:
            words_raw = f.readlines()
            self._words = {word.strip() for word in words_raw}
        with open('../resources/stopwords2.txt', 'r', encoding='utf8') as f:
            words_raw = f.readlines()
            _words_2 = {word.strip() for word in words_raw}
        self._words = self._words.union(_words_2)
        self._decoded_words = {unidecode(word) for word in self._words}


if __name__ == '__main__':
    t_sw = StopWords()
    t_words = t_sw.words
    print(t_words)
    print(t_sw.decoded_words())

