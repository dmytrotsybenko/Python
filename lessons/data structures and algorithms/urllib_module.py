import urllib
from urllib import request, parse


sock = urllib.request.urlopen("https://vk.com/feed")
htmlSource = sock.read().decode('utf-8')
sock.close()
print(htmlSource)
print(sock.info())  # Получение заголовков сервера средствами urllib

data = {"q": "wikipython.ru"}
enc_data = urllib.parse.urlencode(data)

your_url = "http://www.google.ru/"
proxy = {'http': 'http://192.168.0.1:8080'}
f = urllib.request.urlopen(your_url, proxies=proxy)
print(f)