import importlib
from abc import ABCMeta
from pprint import pprint
from typing import List, Dict

import feedparser

from modules.config import SourceSite, Sources
from modules.rss_model import RssArticle


class AbstractRssParser(metaclass=ABCMeta):
    def __init__(self, source: SourceSite):
        self.source = source

    def parse(self) -> List[RssArticle]:
        pass

    def __repr__(self):
        return 'RSS Parser for %s' % self.source.name


class SmeParser(AbstractRssParser):
    def __init__(self, source: SourceSite):
        super().__init__(source)

    def parse(self) -> List[RssArticle]:
        doc = feedparser.parse(self.source.url)
        entries = doc['entries']
        res = []
        for entry in entries:
            title = entry.get('title', '')
            url = entry.get('link', '')
            keywords = entry.get('tags', [])
            perex = entry.get('summary', '')
            res.append(RssArticle(title, url, keywords, perex, '', self.source))
        return res


class PravdaParser(AbstractRssParser):
    def __init__(self, source: SourceSite):
        super().__init__(source)

    def parse(self) -> List[RssArticle]:
        doc = feedparser.parse(self.source.url)
        entries = doc['entries']
        res = []
        for entry in entries:
            print(entry)
            title = entry.get('title', '')
            url = entry.get('link', '')
            keywords = entry.get('keywords', [])
            perex = entry.get('summary', '')
            res.append(RssArticle(title, url, keywords, perex, '', self.source))
        return res


class ParserFactory(object):
    @staticmethod
    def get_parsers(sources: List[SourceSite]) -> Dict[SourceSite, AbstractRssParser]:
        res = {}
        for source in sources:
            parser_class = ParserFactory.get_parser_class(Sources.FEEDS[source.machine_name]['parser'])
            res[source] = parser_class(source)
        return res

    @classmethod
    def get_parser_class(cls, name: str):
        return getattr(importlib.import_module(cls.__module__), name)


if __name__ == '__main__':
    parsers = ParserFactory.get_parsers()
    for parser in parsers:
        pprint(parser.parse())
