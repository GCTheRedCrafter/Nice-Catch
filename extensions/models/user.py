############ extensions/models/user.py
#
#
import json
import uuid
import hashlib
########
#
class User():
    def __init__(self, id: str, username: str, userage: int, dogname: str, dogage: int, dogbreed: str,
                 email: str, password: str, description: str, city: str, mainpicture: str, pictures: list):
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid.uuid4())
        self.username = username
        self.userage = userage
        self.dogname = dogname
        self.dogage = dogage
        self.dogbreed = dogbreed
        self.email = email
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.description = description
        self.city = city
        self.mainpicture = mainpicture
        self.pictures = pictures
    ########
    #
    def check_password(self, tocheck: str):
        return hashlib.sha256(tocheck.encode()).hexdigest() == self.password
    ########
    #
    def load(self):
        try:
            with open('users.json', 'r') as f:
                data = json.load(f)
                userdata = data[self.id]
                
                self.username = userdata['username']
                self.userage = userdata['userage']
                self.dogname = userdata['dogname']
                self.dogage = userdata['dogage']
                self.dogbreed = userdata['dogbreed']
                self.email = userdata['email']
                self.password = userdata['password']
                self.description = userdata['description']
                self.city = userdata['city']
                self.mainpicture = userdata['mainpicture']
                self.pictures = userdata['pictures']
        except Exception as e:
            print(f'Error while loading User: {e}')
    ########
    #
    def save(self):
        try:
            with open('users.json', 'r') as f:
                data = json.load(f)
            with open('users.json', 'w') as f:
                data[self.id]['username'] = self.username
                data[self.id]['userage'] = self.userage
                data[self.id]['dogname'] = self.dogname
                data[self.id]['dogage'] = self.dogage
                data[self.id]['dogbreed'] = self.dogbreed
                data[self.id]['email'] = self.email
                data[self.id]['password'] = self.password
                data[self.id]['description'] = self.description
                data[self.id]['city'] = self.city
                data[self.id]['mainpicture'] = self.mainpicture
                data[self.id]['pictures'] = self.pictures
        except Exception as e:
            print(f'Error while loading User: {e}')

