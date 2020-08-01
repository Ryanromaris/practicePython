import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

today = str(datetime.datetime.now().strftime('20%y%m%d'))
# 오늘날짜

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd='+today, headers=headers)
# 오늘 날짜의 지니차트 불러오기.
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

chart_info = []
for tr in trs:
    rank = tr.select_one('.number').text[0:2].strip()
    title = tr.select_one('.select-check')['title']
    artist = tr.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, 'by' + artist)
    # 달달한맛🍫
    rows = {'rank': rank, 'title': title, 'artist': artist}
    chart_info.append(rows)

db.genie_chart.insert_many(chart_info)
# 짭짤한맛 🍜

