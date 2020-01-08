import requests, json

class Timelines:
    
    def __init__(self, url):

        self.endpoint = url + "/api/v1/timelines/"
    
    def get_public(self, local=False, only_media=0, max_id=-1,
                   since_id=None, min_id=None, limit=20):

        #build the request
        to_send = self.endpoint + "public" + "?local={}&only_media={}&max_id={}&since_id={}&min_id={}&limit={}".format(local, only_media, max_id, since_id, min_id, limit)
        print(to_send)

        #send!
        response = requests.get(to_send)
        unraveled = json.loads(response.text)
        
        return unraveled

my_tl = Timelines("https://mastodon.social")

print(my_tl.get_public())