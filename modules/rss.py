from abc import ABCMeta
from pprint import pprint
from typing import List

import feedparser

from modules.config import Sources


class RssArticle(object):
    def __init__(self, title: str, url: str, keywords: List[str], perex: str, body: str):
        self.title = title
        self.url = url
        self.keywords = keywords
        self.perex = perex
        self.body = body

    def __repr__(self):
        return 'Title: %s\nUrl: %s\nKeywords: %s\nPerex: %s\nBody: %s\n' \
               % (self.title, self.url, self.keywords, self.perex, self.body)


class AbstractRssParser(metaclass=ABCMeta):
    def parse(self) -> List[RssArticle]:
        pass


class SmeParser(AbstractRssParser):
    def __init__(self, url: str):
        self.url = url

    def parse(self) -> List[RssArticle]:
        doc = feedparser.parse(self.url)
        entries = doc['entries']
        res = []
        for entry in entries:
            title = entry.get('title', '')
            url = entry.get('link', '')
            keywords = entry.get('tags', [])
            perex = entry.get('summary', '')
            res.append(RssArticle(title, url, keywords, perex, ''))
        return res


class PravdaParser(AbstractRssParser):
    def __init__(self, url: str):
        self.url = url

    def parse(self) -> List[RssArticle]:
        doc = feedparser.parse(self.url)
        entries = doc['entries']
        res = []
        for entry in entries:
            print(entry)
            title = entry.get('title', '')
            url = entry.get('link', '')
            keywords = entry.get('keywords', [])
            perex = entry.get('summary', '')
            res.append(RssArticle(title, url, keywords, perex, ''))
        return res


class ParserFactory(object):
    @staticmethod
    def get_parsers() -> List[AbstractRssParser]:
        res = []
        for source, data in Sources.FEEDS.items():
            parser_class = getattr(__import__('rss'), data['parser'])
            res.append(parser_class(data['url']))
        return res


if __name__ == '__main__':
    parsers = ParserFactory.get_parsers()
    for parser in parsers:
        pprint(parser.parse())
