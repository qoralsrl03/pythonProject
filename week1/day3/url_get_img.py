# url 을 입력하고 수집 버튼을 누르면 images 해당 url에 있는 이미지를 저장
# 저장시 url 정보와 실제 저장위치 text entry에 출력

from tkinter import *
from bs4 import BeautifulSoup
from urllib import request
import requests
import os

def save_image():
    url = url_entry.get()
    res=requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    img_dir = './images/'

    #저장위치에 폴더 없으면 만들기
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    img_all = soup.find_all('img')

    for i, v in enumerate(img_all):
        if v.get('src'):
            request.urlretrieve(v.get('src'), img_dir + str(i) + '.png')

            text.insert(INSERT, 'Downloads:'+img_dir + str(i) + '.png' +'/ link:'+ v.get('src')+'\n')


    print('img 저장')
    print(img_dir)



app = Tk()
url_entry = Entry(app, width=100)
url_entry.pack()
save_btn = Button(app, text='save img', command=save_image)
save_btn.pack()
text = Text(app, width=100, height=50)
text.pack()
app.mainloop()

