import os
import time
from slackclient import SlackClient
from modules.wht import WHT


class Slack(object):
    def __init__(self, wht_client: WHT):
        self.bot_name = 'whats-happening-today'
        self.slack_client = SlackClient(os.environ.get('WHT_SLACK_BOT_TOKEN'))
        self.websocket_delay = 1 # 1 second delay between reading from firehose
        self.bot_id = os.environ.get('WHT_SLACK_BOT_ID')
        self.at_bot = "<@" + self.bot_id + ">"
        self.command = 'lets read'
        self.wht_client = wht_client

    def get_bot_id(self) -> str:
        """ Get slack bot ID
        """
        slack_client = SlackClient(os.environ.get('WHT_SLACK_BOT_TOKEN'))
        api_call = slack_client.api_call("users.list")
        if api_call.get('ok'):
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == self.bot_name:
                    return user.get('id')

    def listen(self):
        if self.slack_client.rtm_connect():
            print("SlackBot connected and running!")
            while True:
                command, channel = self.parse_slack_output(self.slack_client.rtm_read())
                if command and channel:
                    self.handle_command(command, channel)
                time.sleep(self.websocket_delay)
        else:
            print("Connection failed. Invalid Slack token or bot ID?")

    def handle_command(self, command, channel):
        response = "Not sure what you mean. Use the *" + self.command + "* command."

        if command.startswith(self.command):
            # Get WHT data to send to user
            print("Getting WHT data...")
            msg = ""
            data = self.wht_client.get_trending_data()

            # Trending article
            best_article = data['best_article'] # type: MetaArticle
            msg += "*What's happening today:* \n<{}|{}>".format(best_article.url, best_article.orginal.title)

            # The rest of interestign articles
            trending_articles = ""
            for article in data['trending_articles']:
                trending_articles += "<{}|{}>\n".format(article.url, article.orginal.title)
            msg += "\n\n*Other trending articles*: \n{}\n".format(trending_articles)

            # Trending keywords
            msg += "\n\n*Trending keywords:* {}".format(", ".join(list(data["trending_keywords"])))

        self.slack_client.api_call("chat.postMessage", channel=channel, text=msg, as_user=True)


    def parse_slack_output(self, slack_rtm_output):
          output_list = slack_rtm_output
          if output_list and len(output_list) > 0:
              for output in output_list:
                  if output and 'text' in output and self.at_bot in output['text']:
                      # return text after the @ mention, whitespace removed
                      return output['text'].split(self.at_bot)[1].strip().lower(), \
                             output['channel']
          return None, None


if __name__ == "__main__":
    slack = Slack()
    slack.listen()
