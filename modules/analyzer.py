from modules.datamodel import MetaArticle
from typing import List, Dict
from modules.config import SourceSite
from collections import defaultdict

class Analyzer(object):
    def __init__(self, feeds: Dict[SourceSite, List[MetaArticle]]):
        self.feeds = feeds
        self.trending_articles_count = 3

    def get_keywords_count(self) -> dict:
        """
        Analyze keywords, their counts and occurence.
        :return: dict
         {
            "keyword": {
                "count": x,
                "sources": [],
                "positions": [
                    [i, j, k]
                ]
            }
        }
        """
        keywords = {}
        for i, feed in self.feeds.items():
            for j, article in enumerate(feed):
                for k, word in enumerate(article.keywords + article.title + article.perex):
                    if word in keywords:
                        keywords[word]['count'] += 1
                    else:
                        keywords[word] = {
                            'count': 1,
                            'sources': [],
                            'positions': []
                        }

                    if article.source not in keywords[word]['sources']:
                        keywords[word]['sources'].append(article.source)

                    keywords[word]['positions'].append([i, j, k])
        return keywords

    def get_morst_relevant_data(self, keywords: Dict) -> Dict:
        """
        Get most relevant data based on keyword analysis and intersection of keywords
        :param keywords: from get_keywords_count
        :return: Dict with trending keywords, trending articles and and the best article
        """
        most_sources_keywords = {}

        max_sources = 0
        for word, keyword in keywords.items():
            max_sources = len(keyword['sources']) if len(keyword['sources']) > max_sources else max_sources

        for word, keyword in keywords.items():
            if len(keyword['sources']) == max_sources:
                most_sources_keywords[word] = keyword

        trending_keywords = most_sources_keywords.keys()

        articles_of_interest = []
        for word, keyword in most_sources_keywords.items():
            for position in keyword['positions']:
                articles_of_interest.append(self.feeds[position[0]][position[1]])
        articles_of_interest = set(list(articles_of_interest))

        max_intersect = 0

        # Save articles keyed by number of intersections between article
        # keywords and trending keywords.
        articles_by_keywords_intersect = defaultdict(list)
        for article in articles_of_interest:
            intersect = len(set(article.keywords).intersection(trending_keywords))
            if intersect > max_intersect:
                max_intersect = intersect

            articles_by_keywords_intersect[intersect].append(article)

        # Best article is simply the first one from the max intersect ones.
        best_article = articles_by_keywords_intersect[max_intersect][0]

        # Get remaining max intersect ones, then get remaining number of
        # less interesting ones.
        trending_articles = []
        trending_articles.extend(articles_by_keywords_intersect[max_intersect][1:])

        current_intersect = max_intersect - 1
        while (current_intersect > 0 and len(trending_articles) < self.trending_articles_count):
            articles_needed = self.trending_articles_count - len(trending_articles)
            current_intersect_elements = len(articles_by_keywords_intersect[current_intersect])
            if current_intersect_elements >= articles_needed:
                index = articles_needed
            else:
                index = current_intersect_elements

            trending_articles.extend(articles_by_keywords_intersect[current_intersect][0:index])
            current_intersect -= 1

        return {
            "trending_keywords": trending_keywords,
            "trending_articles": trending_articles,
            "best_article": best_article
        }
