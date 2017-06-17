from typing import List
from unidecode import unidecode
import re

class StringUtils(object):
    @staticmethod
    def to_low_encoded_list(s: str) -> List[str]:
        return [unidecode(w.lower()) for w in StringUtils.remove_noise(s).split(' ')]

    @staticmethod
    def remove_noise(s: str) -> str:
        return re.sub('[.,!?]', '', s)


class ListUtils(object):
    @staticmethod
    def to_low_encoded_list(l: List) -> List[str]:
        return [unidecode(w.lower()) for w in l]
