from pprint import pprint

from modules.config import SourceSite, Sources
from modules.rss import ParserFactory
from modules.datamodel import Collector

if __name__ == '__main__':
    sources = []
    for source, data in Sources.FEEDS.items():
        sources.append(SourceSite(source, data.get(Sources.KEY_NAME, ''), data[Sources.KEY_RSS_URL], data.get(Sources.KEY_BASE_URL, '')))

    pprint(sources)

    parsers = ParserFactory.get_parsers(sources)

    pprint(parsers)

    col = Collector(sources)
    pprint(col.collect())
