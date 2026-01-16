############ extensions/models/user.py
#
#
import json
import uuid
########
#
class Chat():
    def __init__(self, id: str, users: list):
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid.uuid4())
        self.users = users
    ########
    #
    def load(self):
        try:
            with open('data/chats.json', 'r') as f:
                data =  json.load(f)
                self.users = data[self.id]['users']
        except Exception as e:
            print(f'Error while loading Chat: {e}')
    ########
    #
    def save(self):
        try:
            with open('data/chats.json', 'r') as f:
                data =  json.load(f)
            with open('data/chats.json', 'w') as f:
                data[self.id]['users'] = self.users
                json.dump(data, f , indent=3)
        except Exception as e:
            print(f'Error while loading Chat: {e}')
#
#
############