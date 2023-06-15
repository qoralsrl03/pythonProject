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
url = 'https://www.starbucks.co.kr/store/store_map.do'
driver.get(url)
time.sleep(1)
driver.find_element(By.CLASS_NAME,'loca_search').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(5) > a').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#mCSB_2_container > ul > li:nth-child(5) > a').click()
time.sleep(1)
lis = driver.find_elements(By.CSS_SELECTOR,'#mCSB_3_container > ul > li')
total = len(lis)
print('매장 수:',total)
for shop in lis:
    print(shop)
    lat = shop.get_attribute('data-lat')
    long = shop.get_attribute('data-long')
    shopnm = shop.find_element(By.TAG_NAME, 'strong')
    shopinfo = shop.find_element(By.TAG_NAME, 'p')
    shopinfo_text = shopinfo.text
    info = shopinfo_text.split('\n')
    if len(info) == 2:
        addr = info[0]
        hp = info[1]
        print(lat, long, shopnm, shopinfo)


driver.quit()