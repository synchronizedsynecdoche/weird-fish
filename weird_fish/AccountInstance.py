class AccountInstance(object):

    def __init__(self, id, username, acct, display_name,
                 locked, bot, discoverable, group, created_at,
                 note, url, avatar, avatar_static, header,
                 header_static, followers_count, following_count, 
                 statuses_count, last_status_at, emojis, fields):
                 
                 self.id = id
                 self.username = username
                 self.acct = acct
                 self.display_name = display_name

                 self.locked = locked
                 self.bot = bot
                 self.discoverable = discoverable
                 self.group = group
                 self.created_at = created_at

                 self.note = note
                 self.url = url
                 self.avatar = avatar
                 self.avatar_static = avatar_static
                 self.header = header

                 self.header_static = header_static
                 self.followers_count = followers_count
                 self.following_count = following_count

                 self.statuses_count = statuses_count
                 self.last_status_at = last_status_at
                 self.emojis = emojis
                 self.fields = fields

    def intro(self):

        print(f"I am {self.username}, but my friends call me {self.display_name}")