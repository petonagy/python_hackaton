from modules.datamodel import MetaArticle
from typing import List, Dict
from modules.config import SourceSite


class Analyzer(object):
    def __init__(self, feeds: Dict[SourceSite, List[MetaArticle]]):
        self.feeds = feeds

    def get_keywords_count(self) -> dict:
        """
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
                for k, word in enumerate(article.keywords):
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

    def get_articles_score(self, keywords: dict) -> dict:
        """
        :param keywords:
        :return:
        {
            "keyword": {
                "count": x,
                "feeds_count": y
            }
        }
        """
        # min_number_sources = max(len(self.feeds) / 2, 2)
        pass


# if __name__ == '__main__':
