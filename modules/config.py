class RssSources(object):
    FEEDS = {
        'sme': {
            'url': 'http://rss.sme.sk/rss/rss.asp?id=frontpage',
            'parser': 'SmeParser',
        },
        'pravda': {
            'url': 'https://spravy.pravda.sk/rss/xml/',
            'parser': 'PravdaParser',
        }
    }
