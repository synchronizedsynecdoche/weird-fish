import requests
from Accounts import Accounts

class weird_fish:
    def __init__(self, url: str ="https://mastodon.social"):
        self.url = url
        server = Accounts(self.url)
        user = server.get_account(1)
        print(user.intro())

weird_fish()