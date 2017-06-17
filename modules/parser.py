import requests
from lxml import html
from modules.rss import RssArticle
from modules.rss import SmeParser
from modules.rss import RssSources

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
    parser = SmeParser(RssSources.FEEDS['sme'])
    parser = Parser(SmeParser.parse()[0])
    print(parser.get_keywords())

