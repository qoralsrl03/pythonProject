from bs4 import BeautifulSoup
import requests
import re
import csv

url = 'https://movie.daum.net/ranking/boxoffice/weekly'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
arr=[]
lis = soup.select('.box_boxoffice .list_movieranking li')
for li in lis:
    print('=' * 100)
    a=li.select_one('.tit_item a')
    title = a.getText()
    movie_url=a.get('href')
    infos=li.select('.txt_info .info_txt')
    score = re.sub(r'[^0-9,]','',infos[1].getText())
    img = li.select_one('img').get('src')
    arr.append([title,score, movie_url, img])
    print(title)
    print(movie_url)
    print(score)
    print(img)
with open('movie.csv', 'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f,delimiter = '|')
    writer.writerows(arr)
