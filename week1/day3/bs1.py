from bs4 import BeautifulSoup

import requests
url='https://news.naver.com'
res=requests.get(url)
# print(res)
# print(res.status_code)
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)
# print("="*100)
# print(soup.prettify()) #구조화되게(정렬해서 이쁘게) 출력

#이미지 태그만 가져오기
import os
from urllib import request
img_dir='./images/'
if not os.path.exists(img_dir):
    os.mkdir(img_dir)
# 이미지 태그만 가져오기

img_all= soup.find_all('img')
print(img_all)
for i,v in enumerate(img_all):
    if v.get('src'):
        request.urlretrieve(v.get('src'), img_dir + str(1) + '.png')