class Sources(object):
    KEY_RSS_URL = 'rss_url'
    KEY_PARSER = 'parser'
    KEY_BASE_URL = 'base_url'
    KEY_NAME = 'name'
    FEEDS = {
        'sme': {
            KEY_RSS_URL: 'http://rss.sme.sk/rss/rss.asp?id=frontpage',
            KEY_PARSER: 'SmeParser',
            KEY_BASE_URL: 'http://www.sme.sk',
            KEY_NAME: 'Sme',
        },
        'pravda': {
            KEY_RSS_URL: 'https://spravy.pravda.sk/rss/xml/',
            KEY_PARSER: 'PravdaParser',
            KEY_BASE_URL: 'http://www.pravda.sk',
            KEY_NAME: 'Pravda',
        },
        'aktuality': {
            KEY_RSS_URL: 'https://www.aktuality.sk/rss/',
            KEY_PARSER: 'AktualityParser',
            KEY_BASE_URL: 'https://www.aktuality.sk',
            KEY_NAME: 'Aktuality',
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
