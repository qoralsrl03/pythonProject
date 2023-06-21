import re
import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox as messagebox
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f'--user-agent={UA}')

def create_custom_messagebox(window, text, categories):
    text = text
    categories = categories
    category_str = ', '.join(categories)
    result = messagebox.askokcancel('입력 재확인', '검색어: ' + text + '\n선택 카테고리: ' + category_str, parent=window)
    if result:
        # [확인] 버튼을 클릭한 경우 처리할 작업을 수행합니다.
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(3)  # 대기
        if not categories:
            url = f'https://map.naver.com/v5/search/{text}'
        else:
            url = f'https://map.naver.com/v5/search/{text}%20{category_str}'
        driver.get(url)
        time.sleep(3)
        # searchIframe으로 전환
        driver.switch_to.frame('searchIframe')

        lis = []
        for i in range(1, 100):
            selector = f'#_pcmap_list_scroll_container > ul > li:nth-child({i})'
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            if not elements:
                break
            lis.extend(elements)
        time.sleep(1)
        for li in lis:
            name = li.find_element(By.CSS_SELECTOR, 'div.CHC5F > a.tzwk0 > div > div > span.place_bluelink.TYaxT')
            score_elements = li.find_elements(By.CSS_SELECTOR, 'div.CHC5F > div.Dr_06 > div > span.h69bs.a2RFq')

            if len(score_elements) > 0:
                score_text = score_elements[0].text
            else:
                score_text = '-'
            score = re.sub(r'^별점\n', '', score_text)
            category_elements = li.find_elements(By.CSS_SELECTOR,'div.CHC5F > a.tzwk0 > div > div > span.KCMnt')
            if len(category_elements) > 0:
                category = category_elements[0].text
            else:
                category = '-'

            reviews= li.find_elements(By.CSS_SELECTOR,'div.CHC5F > div > div > span:nth-child(3)')
            for review_t in reviews:
                review_text = review_t.text
                review = re.sub(r'\D', '', review_text)  # 숫자 이외의 문자 제거
            print('리뷰:'+ review)
            print('카테고리: '+category)
            print('별점: '+score)
            print('상호명 : '+name.text)
            print('='*100)
        driver.quit()
    else:
        # [취소] 버튼을 클릭한 경우 처리할 작업을 수행합니다.
        messagebox.showinfo("알림", '검색을 취소합니다')

def btn_click():
    text = txt.get()
    selected_indices = listbox.curselection()
    selected_categories = [listbox.get(idx) for idx in selected_indices]
    create_custom_messagebox(window, text, selected_categories)



window = tk.Tk()
window.geometry("900x700+100+100")
window.title("지역 분석")
# 검색 텍스트 영역
txt = tk.Entry(window)
txt.grid(row=0, column=0, sticky='nsew')

# 검색 버튼
btn = tk.Button(window, text='검색', command=btn_click)
btn.grid(row=0, column=1, sticky='nsew')

# 카테고리 리스트 박스
listbox = tk.Listbox(window, selectmode='extended', height=0)
listbox.grid(row=1, column=0, columnspan=2, sticky='nsew')

# 카테고리 데이터 추가 예시
categories = ['음식점', '카페', '주차장', '주유소', '은행', '마트', '헤어샵', '병원']
for category in categories:
    listbox.insert(tk.END, category)

# 글꼴 설정
txt.config(font=('helvetica', 30, 'bold'))
btn.config(font=('helvetica', 30, 'bold'))
listbox.config(font=('helvetica', 30, 'bold'))

# 열과 행의 가중치를 설정하여 크기를 동일하게 키우기
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

window.mainloop()
