############ extensions/models/message.py
#
#
import json
import uuid
from datetime import datetime
########
#
class Message():
    def __init__(self, id: str, text: str, writerid: str, chatid: str):
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid.uuid4())
        self.date = datetime.strftime(datetime.now(), '%d/%m/%Y, %H:%M:%S')
        self.text = text
        self.writerid = writerid
        self.chatid = chatid
    ########
    #
    def load(self):
        try:
            with open('data/messages.json', 'r') as f:
                data = json.load(f)
                self.text = data[self.id]['text']
                self.writerid = data[self.id]['writerid']
                self.chatid = data[self.id]['chatid']
        except Exception as e:
            print(f'Error while loading Message: {e}')
    ########
    #
    def save(self):
        try:
            with open('data/message.json', 'r') as f:
                data = json.load(f)
            with open('data/messages.json', 'w') as f:
                data[self.id]['text'] = self.text
                data[self.id]['writerid'] = self.writerid
                data[self.id]['chatid'] = self.chatid
                json.dump(data, f, indent=3)
        except Exception as e:
            print(f'Error while saving Message: {e}')