from typing import Set

from pkg_resources import resource_filename
from unidecode import unidecode

from resources import resources


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
        with open(resource_filename(resources.Resources.__module__, 'stopwords1.txt'), 'r', encoding='utf8') as f:
            words_raw = f.readlines()
            cls._words = {word.strip() for word in words_raw}
        with open(resource_filename(resources.Resources.__module__, 'stopwords2.txt'), 'r', encoding='utf8') as f:
            words_raw = f.readlines()
            _words_2 = {word.strip() for word in words_raw}
        cls._words = cls._words.union(_words_2)
        cls._decoded_words = {unidecode(word) for word in cls._words}
