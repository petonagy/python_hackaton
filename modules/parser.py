import requests
from lxml import html

from modules.config import SourceSite
from modules.rss import ParserFactory, RssArticle, Sources
from modules.utils import StringUtils


class Parser(object):
    def __init__(self, article: RssArticle):
        self.url = article.url

    def get_document(self) -> str:
        return requests.get(self.url).content

    def get_keywords(self) -> list:
        tree = html.fromstring(self.get_document())
        keywords = tree.xpath('/html/head/meta[@name="keywords"]/@content')

        return StringUtils.to_low_encoded_list(keywords)


if __name__ == '__main__':
    sources = []
    for source, data in Sources.FEEDS.items():
        sources.append(SourceSite(source, data.get('name', ''), data['rss_url'], data.get('base_url', '')))

    parsers = ParserFactory.get_parsers(sources)

    for source, parser in parsers.items():
        html_parser = Parser(parser.parse()[0])
        print(html_parser.get_keywords())

