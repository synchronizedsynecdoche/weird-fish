import json

import requests

class Timelines:
    
    def __init__(self, url):

        self.endpoint = url + "/api/v1/timelines/"
    
    def get_public(self, local=False, only_media=False, max_id=0,
                   since_id=0, min_id=0, limit=20):
    
        """Gets the latest public posts from the timeline (what you see on the homepage)

        Args:
            local: Do we want to get posts from other nodes our instance is federated with?
            
            only_media: Do we want to only see posts containing media?

            max_id: Maximum (API) ID to fetch, note that the ID seen on an instance's website is not necessarily the ID used by the API

            since_id: Earliest API ID to fetch.

            min_id: Minimum API ID to fetch.

            limit: How many posts do we want? Vanilla Mastodon defaults to 20.

        Returns: 
            A Python dictionary from the JSON returned by /api/v1/timelines/public

        Raises:

            A ValueError when passed IDs that won't be understood by Mastodon.

        """
        
        if since_id < min_id or min_id > max_id or min_id < 0:
            raise ValueError("min_id must be less than since_id and max_id and all must be at least 0")

        

        #build the request
        to_send = self.endpoint + f"public?local={local}&only_media={only_media}&limit={limit}"
        
        if max_id:
            to_send += f"&max_id={max_id}".format(max_id)

        if min_id:
            to_send += f"&min_id={min_id}"

        if since_id:
            to_send += f"&since_id={since_id}"

        #send!
        response = requests.get(to_send)

        unraveled = json.loads(response.text)
        
        return unraveled