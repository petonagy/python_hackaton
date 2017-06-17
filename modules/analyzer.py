from modules.datamodel import MetaArticle

class Analyzer(object):
    def __init__(self, articles: list[list[MetaArticle]]):
        self.articles = articles

    def get_keywords_count(self) -> list:
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
        for i, feed in enumerate(self.articles):
            for j, article in enumerate(feed):
                for k, word in enumerate(article.keywords):
                    pass

    def get__keywords_score(self, keywords: dict) -> dict:
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
