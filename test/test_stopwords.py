import unittest

from modules.stopwords import StopWords


class StopWordsTest(unittest.TestCase):
    def stopwords_test(self):
        self.assertIn('túto', StopWords.get_words())
        self.assertIn('tuto', StopWords.get_decoded_words())
        self.assertNotIn('počítač', StopWords.get_words())
        self.assertNotIn('pocitac', StopWords.get_decoded_words())
        self.assertGreater(len(StopWords.get_words()), 10)
        self.assertGreater(len(StopWords.get_decoded_words()), 10)


if __name__ == '__main__':
    unittest.main()
