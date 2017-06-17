from typing import List, Dict

from modules.config import SourceSite
from modules.rss import ParserFactory
from modules.rss_model import RssArticle
from modules.utils import StringUtils
from modules.utils import ListUtils
from modules.parser import Parser


class MetaArticle(object):
    """ Meta representation of an article, in which all key fields are parsed to lowercase strings without accents. """

    def __init__(self, title: List[str], url: str, keywords: List[str], perex: List[str], body: str,
                 source: SourceSite):
        self.title = title
        self.url = url
        self.keywords = keywords
        self.perex = perex
        self.body = body
        self.source = source

    def __repr__(self):
        return 'Title: %s\nUrl: %s\nKeywords: %s\nPerex: %s\nBody: %s\nSource: %s' \
               % (self.title, self.url, self.keywords, self.perex, self.body, self.source.name)


class MetaArticleFactory(object):
    @staticmethod
    def from_rss_article(a: RssArticle) -> MetaArticle:
        return MetaArticle(
            title=StringUtils.remove_stopwords(StringUtils.to_low_encoded_list(a.title)),
            url=a.url,
            keywords=StringUtils.remove_stopwords(ListUtils.to_low_encoded_list(a.keywords)),
            perex=StringUtils.remove_stopwords(StringUtils.to_low_encoded_list(a.perex)),
            body=a.body,
            source=a.source
        )


class Collector(object):
    def __init__(self, sources: List[SourceSite]):
        self.sources = sources
        self.parsers = ParserFactory.get_parsers(self.sources)

    def collect(self) -> Dict[SourceSite, List[MetaArticle]]:
        res = {}
        for source, parser in self.parsers.items():
            articles = []
            for rss_article in parser.parse():
                meta_article = MetaArticleFactory.from_rss_article(rss_article)
                html_parser = Parser(rss_article)
                meta_article.keywords += html_parser.get_keywords()
                articles.append(meta_article)
            res[source] = articles
        return res
