from typing import Set

from unidecode import unidecode
import unittest

class StopWords(object):
    _words = None
    _decoded_words = None

    @classmethod
    def get_words(cls) -> Set[str]:
        if cls._words is None or cls._words is None:
            cls._load()
        return set(cls._words)

    @classmethod
    def get_decoded_words(cls) -> Set[str]:
        if cls._words is None or cls._words is None:
            cls._load()
        return set(cls._decoded_words)

    @classmethod
    def _load(cls):
        with open('../resources/stopwords1.txt', 'r', encoding='utf8') as f:
            words_raw = f.readlines()
            cls._words = {word.strip() for word in words_raw}
        with open('../resources/stopwords2.txt', 'r', encoding='utf8') as f:
            words_raw = f.readlines()
            _words_2 = {word.strip() for word in words_raw}
        cls._words = cls._words.union(_words_2)
        cls._decoded_words = {unidecode(word) for word in cls._words}


if __name__ == '__main__':
    # print(StopWords.get_words())
    # print(StopWords.get_decoded_words())
    unittest.main()


class StopWordsTest(unittest.TestCase):
    def stopwords_test(self):
        self.assertIn('túto', StopWords.get_words())
