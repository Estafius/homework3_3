from pprint import pprint

import vk
from urllib.parse import urlencode, urlparse
import requests


AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.63'
APP_ID = 5949170    # Your app_id here

token_url = 'https://oauth.vk.com/blank.html#access_token=be55f62a549c29e1a8cca264fa4ccd433741d71ba1108a4078a641be3cde584e3d2063509b232b9b7ec1d&expires_in=86400&user_id=7209446'

o = urlparse(token_url)
fragments = dict((i.split('=') for i in o.fragment.split('&')))
access_token = fragments['access_token']

params = {'access_token': access_token,
          'v': VERSION,
          }


def get_my_friend_list(user_id=None):
     params['user_id'] = user_id
     response = requests.get('https://api.vk.com/method/friends.get',params)
     my_friends_list = response.json()['response']['items']
     for friend in my_friends_list:
      params_my_friends = {'access_token': access_token,
                  'v': VERSION,
                  'user_id' : friend,
                  }
      response_my_friends = requests.get('https://api.vk.com/method/friends.get', params_my_friends)
      print("Общие друзья", list(set(my_friends_list) & set(response_my_friends.json()['response']['items'])))

get_my_friend_list()