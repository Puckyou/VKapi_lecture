import requests
from urllib.parse import urlencode


APP_ID = 6085717
VERSION = "5.65"
KEY = "RzdaD3cf57GK8xCzXG4u"

def oauth_link():
    AOTH_URL = "https://oauth.vk.com/authorize"
    auth_data = {
    "client_id" : APP_ID,
    "response_type" : "token",
    "scope" : "friends",
    "v" : VERSION
    }
    return "?".join((AOTH_URL, urlencode(auth_data)))

TOKEN = ""

def get_freind_l():
    param = {
        "access_token" : TOKEN,
        "v" : VERSION
    }

    response = requests.get("https://api.vk.com/method/friends.get", param)
    return response.json()["response"]["items"]


def collect_friends(user_id):
    param = {
        "access_token": TOKEN,
        "v": VERSION,
        "user_id" : user_id
    }

    response = requests.get("https://api.vk.com/method/friends.get", param)
    return response.json()["response"]["items"]

friend_list = get_freind_l()

all_my_friends = {}
for friend in friend_list:
    try:
        all_my_friends[friend] = collect_friends(friend)
    except:
        pass

a = set.intersection(*(set(val) for val in all_my_friends.values()))
print("Общие друзья:{}".format(", ".join(str(e) for e in a)))
