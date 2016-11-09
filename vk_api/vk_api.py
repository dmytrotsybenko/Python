import os
import vk
import json
from urllib.request import urlopen

my_apiid = '5706347'
user_login = 'meageinsttoworld@gmail.com'
password = 'zxcvbnmzxcvbnm'


address = 'https://api.vk.com/method/audio.get?owner_id=28818435&access_token=303919345db373556661d031cfa69f494ad9a5957e98c9b95ca556ab96666ce333e8c4c562ee68a56c6a2'
data = urlopen(address)
decode_response = data.read().decode()
final_data = json.loads(decode_response)
# print(final_data)
songs = final_data['response'][1:4]
for _, song in enumerate(songs):
    print(song)
    song_artist = song['artist']
    song_title = song['title']
    song_url = song['url']
    cashed_song = urlopen(song_url).read()
# os.mkdir('C://Music')
# if song_artist not in os.listdir('C://Music'):
#     os.mkdir('C://Music/%s' %(song_artist))
    file_is_here = '%s.mp3'%(song_title)
    filename = 'C://Music/%s.mp3' %(song_title)
    if file_is_here in os.listdir('C:\Music'):
        print("File not empty")
    else:
        print("else case")
        # file = open(filename, 'wb')
        # file.write(cashed_song)
        # file.close()

# vkapi = vk.API(my_apiid, user_login, password)
# vkapi.access_token = s
# vk.api.wall.post(message='Hi, my first vk api')
