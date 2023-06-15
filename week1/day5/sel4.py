#팝업이 있는 페이지의 경우 팝업 닫기
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from bs4 import BeautifulSoup


chromedriver_autoinstaller.install()
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) # 대기
url = 'http://127.0.0.1:5500/ex-public/seltest/test2.html'
driver.get(url)
time.sleep(1)
window_handler = driver.window_handles
driver.switch_to.window(window_handler[1]) #[0] 번째가 부모(최초 페이지)
time.sleep(1)
driver.find_element(By.ID,'btn').click()
time.sleep(1)
driver.switch_to.window(window_handler[0])
driver.execute_script('fn_check()') #해당 페이지의 함수 호출

div = driver.find_element(By.ID, 'div_id')
lis = div.find_elements(By.TAG_NAME,'li')
for li in lis:
    print(li.text)
time.sleep(3)
driver.quit()