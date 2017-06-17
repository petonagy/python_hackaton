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


class SourceSite(object):
    def __init__(self, machine_name: str, name: str, url: str):
        self.machine_name = machine_name
        self.name = name
        self.url = url

    def __repr__(self):
        return '%s (%s) @ %s' % (self.name, self.machine_name, self.url)
