import praw as rawr
import urllib.request
from secrets.secret_function9 import Client_Secret_9

client_secret = Client_Secret_9()

def reddit_image_succ(url):
    rro = rawr.Reddit(client_id="5Qs9v2C52q_yEg",         # your client id
                                client_secret=client_secret._secret,      # your client secret
                                user_agent="Beeb89praw")        # your user agent

    submission = rro.submission(url=url)
    pic = submission.url
    name = pic.split('/')
    urllib.request.urlretrieve(pic, name[-1])
