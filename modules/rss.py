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

    def __repr__(self):
        return 'Title: %s\nUrl: %s\nKeywords: %s\nPerex: %s\nBody: %s\n' \
               % (self.title, self.url, self.keywords, self.perex, self.body)


class SmeParser(object):
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


if __name__ == '__main__':
    parser = SmeParser(RssSources.FEEDS['sme'])
    pprint(parser.parse())
