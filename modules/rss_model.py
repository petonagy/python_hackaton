from typing import List
from modules.config import SourceSite


class RssArticle(object):
    def __init__(self, title: str, url: str, keywords: List[str], perex: str, body: str, source: SourceSite):
        self.title = title
        self.url = url
        self.keywords = keywords
        self.perex = perex
        self.body = body
        self.source = source

    def __repr__(self):
        return 'Title: %s\nUrl: %s\nKeywords: %s\nPerex: %s\nBody: %s\nSource: %s' \
               % (self.title, self.url, self.keywords, self.perex, self.body, self.source.name)
