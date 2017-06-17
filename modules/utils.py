from typing import List
from unidecode import unidecode


class StringUtils(object):
    @staticmethod
    def to_low_encoded_list(s: str) -> List[str]:
        return [unidecode(w.lower()) for w in s]
