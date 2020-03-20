from AccountInstance import AccountInstance

import json

import requests

class Accounts:
    
    def __init__(self, url):

        self.endpoint = url + "/api/v1/accounts/"

    
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

        response = requests.get(self.endpoint + str(id))

        if response.status_code == 410:
            
            raise RuntimeError(f"Account with ID {id} is suspended!")

        if not response.ok:
            print(self.endpoint + str(id))
            raise RuntimeError(f"Bad response from {self.endpoint + str(id)}")

        unraveled = json.loads(response.text)
        
        if not account_object:
            return unraveled
        

        return AccountInstance(response.text)