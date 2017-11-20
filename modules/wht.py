from modules.config import SourceSite, Sources
from modules.rss import ParserFactory
from modules.datamodel import Collector
from modules.analyzer import Analyzer
from requests import request
from modules.datamodel import MetaArticle

class WHT(object):
    """ What is Happening Today (WHT) bundle """

    def get_trending_data(self):
        sources = []
        for source, data in Sources.FEEDS.items():
            sources.append(SourceSite(source, data.get('name', ''), data['rss_url'], data.get('base_url', '')))

        parsers = ParserFactory.get_parsers(sources)

        col = Collector(sources)
        entries = col.collect()

        # Analyze keywords
        analyzer = Analyzer(entries)
        keywords = analyzer.get_keywords_count()

        data = analyzer.get_morst_relevant_data(keywords)

        return data
