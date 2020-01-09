from AccountInstance import AccountInstance

import json

import requests

class Accounts:
    
    def __init__(self, url):

        self.endpoint = url + "/api/v1/accounts/"

    
    def object_encoder(self, info):

        """ Encode the json from get_account in an object for easier use 

            Args:
                info: the serialized JSON response
            
            Returns:
                an AccountInstance object populated with the data 
        """
        
        return AccountInstance(info['id'], info['username'], info['acct'], info['display_name'], info['locked'], info['bot'],info['discoverable'],
                               info['group'],info['created_at'],info['note'],info['url'], info['avatar'], info['avatar_static'],info['header'],
                               info['header_static'], info['followers_count'], info['following_count'], info['statuses_count'],info['last_status_at'],
                                info['emojis'], info['fields'])

    
    def get_account(self, id, account_object=True):

        """Gets publically available information about an account

        Args:
            id: the id of the user
            
            account_object: optional, specifies whether to return a dictionary or an AccountInstance object

        Returns: 
            
            account_object=False: A Python dictionary from the JSON returned by /api/v1/accounts/

            account_object=True: An AccountInstance object populated with the data from /api/v1/accounts

        Raises:

            A ValueError when passed IDs that won't be understood by Mastodon.

            A RuntimeError when an ID refers to a suspended account, or when a request fails (i.e. 404)

        """

        if id < 0:
            raise ValueError("Bad ID: IDs must be at least 0")


        response = requests.get(self.endpoint + str(id))

        if response.status_code == 410:
            
            raise RuntimeError(f"Account with ID {id} is suspended!")

        if not response.ok:

            raise RuntimeError(f"Bad response from {self.endpoint}")

        unraveled = json.loads(response.text)
        
        if not account_object:
            return unraveled
        

        return self.object_encoder(unraveled)