import feedparser
from typing import List
from pprint import pprint
from modules.data import RssSources


class RssArticle(object):
    def __init__(self, title: str, url: str, keywords: List[str], perex: str, body: str):
        self.title = title
        self.url = url
        self.keywords = keywords
        self.perex = perex
        self.body = body


class SmeParser(object):
    def __init__(self, url: str):
        self.url = url

    def parse(self) -> List[RssArticle]:
        doc = feedparser.parse(self.url)
        entries = doc['entries']
        pprint(entries)
        return []


if __name__ == '__main__':
    parser = SmeParser(RssSources.FEEDS['sme'])
    parser.parse()
