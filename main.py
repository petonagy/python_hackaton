from modules.slack import Slack
from modules.wht import WHT

if __name__ == '__main__':
    wht_client = WHT()

    slack_client = Slack(wht_client)
    slack_client.listen()
