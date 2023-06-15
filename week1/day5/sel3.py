#얼럿이 노출되서 안넘어가는 페이지의 경우 얼럿 자동 닫기
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from bs4 import BeautifulSoup


chromedriver_autoinstaller.install()
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) # 대기
url = 'http://127.0.0.1:5500/ex-public/seltest/test.html'
driver.get(url)
alert = Alert(driver) #alert 창이 나타날때까지 대기
print(alert.text)
alert.accept() # 확인버튼
#만약 confirm 일경우 취소는 dismiss()

div = driver.find_element(By.ID, 'div_id')
lis = div.find_elements(By.TAG_NAME,'li')
for li in lis:
    print(li.text)
driver.quit()