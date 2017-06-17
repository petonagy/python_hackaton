from modules.config import Sources
from modules.datamodel import SourceSite
from pprint import pprint

if __name__ == '__main__':
    sources = []
    for source, data in Sources.FEEDS.items():
        sources.append(SourceSite(source, data.get('name', ''), data['base_url']))

    pprint(sources)
