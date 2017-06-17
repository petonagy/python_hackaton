class Sources(object):
    FEEDS = {
        'sme': {
            'url': 'http://rss.sme.sk/rss/rss.asp?id=frontpage',
            'parser': 'SmeParser',
            'base_url': 'http://www.sme.sk',
            'name': 'Sme',
        },
        'pravda': {
            'url': 'https://spravy.pravda.sk/rss/xml/',
            'parser': 'PravdaParser',
            'base_url': 'http://www.pravda.sk',
            'name': 'Pravda',
        }
    }
