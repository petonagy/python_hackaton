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
                "sources_num": y
            }
        }
        """
        keywords = {}
        for i, feed in enumerate(self.feeds):
            keywords[word]['sources_num'] += 1
            for j, article in enumerate(feed):
                for k, word in enumerate(article.keywords):
                    if word in keywords:
                        keywords[word]['count'] += 1
                    else:
                        keywords[word]['count'] = 1
                    keywords[word]['positions'].append([i, j, k])
        return keywords

    def get_articles_score(keywords: dict) -> dict:
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
        # min_number_sources = max(len(sources) / 2, 2)
        pass
