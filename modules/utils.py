import re
import unittest
from typing import List

from unidecode import unidecode

from modules.stopwords import StopWords


class StringUtils(object):
    @staticmethod
    def to_low_encoded_list(s: str) -> List[str]:
        return [unidecode(w.lower()) for w in StringUtils.remove_noise(s).split(' ')]

    @staticmethod
    def remove_noise(s: str) -> str:
        return re.sub('[.,!?]', '', s)

    @staticmethod
    def remove_stopwords(words: List[str]) -> List[str]:
        return [word for word in words if
                (word not in StopWords.get_words() and word not in StopWords.get_decoded_words())]


class ListUtils(object):
    @staticmethod
    def to_low_encoded_list(l: List) -> List[str]:
        return [unidecode(w.lower()) for w in l]


if __name__ == '__main__':
    unittest.main()


class StringUtilsTest(unittest.TestCase):
    def stopwords_test(self):
        self.assertEquals(StringUtils.remove_stopwords(['ten', 'každý', 'kazdy', 'počítač']), ['počítač'])
