from pprint import pprint

from modules.config import SourceSite, Sources
from modules.rss import ParserFactory
from modules.datamodel import Collector
from modules.analyzer import Analyzer
from requests import request
from lxml.html import fromstring

if __name__ == '__main__':
    sources = []
    for source, data in Sources.FEEDS.items():
        sources.append(SourceSite(source, data.get('name', ''), data['rss_url'], data.get('base_url', '')))

    # pprint(sources)

    parsers = ParserFactory.get_parsers(sources)

    # pprint(parsers)

    col = Collector(sources)
    entries = col.collect()

    # pprint(entries)

    analyzer = Analyzer(entries)
    keywords = analyzer.get_keywords_count()
    # pprint(keywords)

    data = analyzer.get_morst_relevant_data(keywords)
    pprint(data)

    r = request('GET', data['best_article'].url)
    tree = fromstring(r.content)
    title = tree.findtext('.//title')
    text = "What's happening today: {}\n\n{}".format(title, data['best_article'].url)

    request('GET', 'https://slack.com/api/chat.postMessage?token=xoxp-87076484640-87088670897-121376898595-f020c7663ad965c5ed1a3722bcec15a8&channel=python-hacks&text={}&pretty=1'.format(text))

