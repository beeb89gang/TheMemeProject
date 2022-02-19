from secrets.secret_function6 import Client_Secret_6
import os
client_secret_2 = os.environ.get("reddit_key_2")

class Client_Secret_9(Client_Secret_6):
    h = client_secret_2

    def __init__(self):
        super()
        self._secret = self._notthesecret + bytes.fromhex(self.h).decode('utf-8')
        
        print('LMAO', self._secret)