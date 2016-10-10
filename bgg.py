import xml.etree.ElementTree as ET
import requests
from time import sleep

user_name = 'dlutsch'
params = {'wanttoplay': '1', 'wanttobuy': '0', 'wantintrade': '0', 'wishlist': '0'}
user = requests.get(url='https://www.boardgamegeek.com/xmlapi/collection/%s' % user_name, params=params)
while user.status_code != 200:
    sleep(1)
    print(user.status_code)
    user = requests.get(url='https://www.boardgamegeek.com/xmlapi/collection/%s' % user_name, params=params)

user_root = ET.fromstring(user.text)
want_to_play = []
for game in user_root:
    want_to_play.append(game.find('name').text)


print(want_to_play)

vpc = requests.get('https://www.boardgamegeek.com/xmlapi/collection/victorypointcafe?own=1&subtype=boardgame')
while vpc.status_code != 200:
    sleep(1)
    print(vpc.status_code)
    vpc = requests.get('https://www.boardgamegeek.com/xmlapi/collection/victorypointcafe?own=1&subtype=boardgame')

vpc_root = ET.fromstring(vpc.text)
vpc_owned = []
for game in vpc_root:
    vpc_owned.append(game.find('name').text)

for game in want_to_play:
    if game in vpc_owned:
        print(game)
