import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

raw = BeautifulSoup(data.text, 'html.parser')
ranks = raw.select('#regularTeamRecordList_table > tr')

for rank in ranks:
    temp = rank.select_one('td.tm > div')
    if temp is not None:
        num = rank.select_one('th>strong').text
        name = temp.select_one('span').text

        print(num +" "+ name)