class Sources(object):
    FEEDS = {
        'sme': {
            'rss_url': 'http://rss.sme.sk/rss/rss.asp?id=frontpage',
            'parser': 'SmeParser',
            'base_url': 'http://www.sme.sk',
            'name': 'Sme',
        },
        'pravda': {
            'rss_url': 'http://spravy.pravda.sk/rss/xml/',
            'parser': 'PravdaParser',
            'base_url': 'http://www.pravda.sk',
            'name': 'Pravda',
        },
        'aktuality': {
            'rss_url': 'http://www.aktuality.sk/rss/',
            'parser': 'AktualityParser',
            'base_url': 'http://www.aktuality.sk',
            'name': 'Aktuality',
        }
    }


class SourceSite(object):
    def __init__(self, machine_name: str, name: str, rss_url: str, base_url: str):
        self.machine_name = machine_name
        self.name = name
        self.rss_url = rss_url
        self.base_url = base_url

    def __repr__(self):
        return '%s (%s) @ %s [%s]' % (self.name, self.machine_name, self.rss_url, self.base_url)
