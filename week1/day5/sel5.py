from selenium.webdriver.common.keys import Keys
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
url = 'https://www.pexels.com/ko-kr/search/4k%20%EB%B0%B0%EA%B2%BD%ED%99%94%EB%A9%B4/'
driver.get(url)
time.sleep(1)
try:
    cnt = 15
    pagedown = 1
    body = driver.find_element(By.TAG_NAME, 'body')
    while pagedown < cnt:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        pagedown += 1
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.prettify())
except Exception as e:
    print(str(e))