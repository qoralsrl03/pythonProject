#Selenium 사용법
#-chromedriver 사이트에서 내 크롬버전과 똑같은 버전(맨 뒤 소수점은 상관없음)을 다운받아 작업할 프로젝트와 같은 폴더에 위치시킴
# pip install selenium
# pip install chromedriver_autoinstaller
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


chromedriver_autoinstaller.install()
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) # 대기
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
div = soup.select_one('#tb_list')
trs = div.find_all('tr')
for i, tr in enumerate(trs):
    if i > 0:
        print('='*100)
        a= tr.find('span', class_='rank').text
        b = tr.find_all('td')[5].select_one('a').getText()
        print(a+' 등: ', b)


# div = driver.find_element(By.ID, 'tb_list')
# trs = div.find_elements(By.TAG_NAME,'tr')
# for tr in trs:
#     print(tr.get_attribute('data-song-no'))


driver.quit()