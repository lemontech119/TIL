import requests
from bs4 import BeautifulSoup

url = 'https://music.naver.com/listen/top100.nhn?domain=TOTAL_V2'
music_url = 'https://music.naver.com/lyric/index.nhn?trackId='
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

item = soup.select("._title")
href_list = []
for top_list in item:
    href = top_list.get('href')
    href = href.replace("#", "")
    href_list.append(href)

f = open('test.txt', mode='wt', encoding='utf-8')
data = ""
for lyric in  href_list:
    response = requests.get(music_url + lyric).text
    soup = BeautifulSoup(response, 'html.parser')
    lyricText = soup.select_one("#lyricText").text
    data = data + lyricText
f.write(data)