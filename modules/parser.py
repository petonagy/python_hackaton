import requests
from unidecode import unidecode
from lxml import html


class Parser(object):
    def __init__(self, url):
        self.url = url

    def get_document(self):
        return requests.get(self.url).content

    def get_keywords(self):
        tree = html.fromstring(self.get_document())

        keywords = tree.xpath('/html/head/meta[@name="keywords"]/@content')

        return [unidecode(keyword.lower()) for keyword in keywords]


if __name__ == '__main__':
    parser = Parser('http://s.sme.sk/r-rss/20557963/svet.sme.sk/syria-ani-irak-nie-su-statmi-su-to-uzemia-na-ktorych-sa-da-zbohatnut.html')
    print(parser.get_keywords())

