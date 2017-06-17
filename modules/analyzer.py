from modules.datamodel import MetaArticle

class Analyzer(object):
    def __init__(self, feeds: list[list[MetaArticle]]):
        self.feeds = feeds

    def get_keywords_count(self) -> dict:
        """
        :return: dict
         {
            "keyword": {
                "count": x,
                "positions": [
                    [i, j, k]
                ]
            }
        }
        """
        keywords = {}
        for i, feed in enumerate(self.feeds):
            for j, article in enumerate(feed):
                for k, word in enumerate(article.keywords):
                    if word in keywords:
                        keywords[word]['count'] += 1
                    else:
                        keywords[word]['count'] = 1
                    keywords[word]['positions'].append([i, j, k])
        return keywords

    @staticmethod
    def get_keywords_score(keywords: dict) -> dict:
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
        pass
