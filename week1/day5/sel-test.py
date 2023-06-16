import chromedriver_autoinstaller
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import util
from PIL import Image

chromedriver_autoinstaller.install()
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) # 대기
url = 'https://finance.naver.com/item/main.naver?code=339770#'
driver.get(url)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#chart_area > div.chart > div > dl.bar > dd > ul > li.month > a').click()
time.sleep(1)
element = driver.find_element(By.CSS_SELECTOR, '#img_chart_area')
# 요소의 위치와 크기 가져오기
location = element.location
size = element.size

# 좌표값 계산
left = location['x']
top = location['y']
right = left + size['width']
bottom = top + size['height']

# 좌표값 출력
print('Left:', left)
print('Top:', top)
print('Right:', right)
print('Bottom:', bottom)

util.fullpage_screenshot(driver,'test2.png');
screenshot = Image.open('test2.png')
cropped_image = screenshot.crop((left, top, right, bottom))
cropped_image.save('cropped_image.png')
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,'#content > div.section.new_bbs > div.sub_section.right > a').click()
time.sleep(1)
trs_selector = '#content > div.section.inner_sub > table.type2 > tbody > tr'
trs = driver.find_elements(By.CSS_SELECTOR, trs_selector)
for i, tr in enumerate(trs):
    if i >= 3:
        try:
            element = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(1) > span')
            element2_selector = f'{trs_selector}:nth-child({i}) > td.title > a'
            element2 = driver.find_element(By.CSS_SELECTOR, element2_selector)
            date = element.text
            text = element2.text
            print(date, text)
        except NoSuchElementException:
            pass
        time.sleep(3)

#content > div.section.inner_sub > table.type2 > tbody > tr:nth-child(3) > td.title > a
#content > div.section.inner_sub > table.type2 > tbody > tr:nth-child(4) > td.title > a
