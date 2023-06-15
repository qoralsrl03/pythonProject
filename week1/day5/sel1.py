#Selenium 사용법
#-chromedriver 사이트에서 내 크롬버전과 똑같은 버전(맨 뒤 소수점은 상관없음)을 다운받아 작업할 프로젝트와 같은 폴더에 위치시킴
# pip install selenium
# pip install chromedriver_autoinstaller
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chromedriver_autoinstaller.install()
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) # 대기
url = 'https://www.hanatour.com'
driver.get(url)
time.sleep(1)

driver.find_element(By.ID,'input_keyword').send_keys('하와이')
driver.find_element(By.CSS_SELECTOR,'button.btn_search').click()
time.sleep(3)


driver.quit()