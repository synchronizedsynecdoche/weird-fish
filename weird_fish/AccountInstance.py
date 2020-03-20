
import json


class AccountInstance(object):


    BEGINNING_OF_TIME = 0
    ego = None 
    def __init__(self, json_obj):
        self.ego = json.loads(json_obj)

    def intro(self):

        if self.ego is None:
            print("Caught a bad ego")
            return
        print(f"I am {self.ego['username']}, but my friends call me {self.ego['display_name']}")
