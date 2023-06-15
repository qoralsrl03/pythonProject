import requests
from bs4 import BeautifulSoup
import cx_Oracle
conn = cx_Oracle.connect('java', 'oracle', 'localhost:1521/xe')

sql = """
    MERGE INTO musinsa a
    USING DUAL b
    ON (a.seq = :seq)
    WHEN MATCHED THEN   -- 있을 경우
         UPDATE SET a.hit = :hit
                , a.r_dt = :r_dt
    WHEN NOT MATCHED THEN --없을 경우
        INSERT VALUES(:seq, :title, :cate, :hit, :r_dt, :url)
"""
with conn:
    for idx in range(1, 100):
        print(idx, "page", "=" * 100)
        url = 'https://www.musinsa.com/mz/community?p=' + str(idx)
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        print(soup.prettify())
        div = soup.find('div', class_='list_content')
        lis = div.find_all('li')
        for i, li in enumerate(lis):
            # print('='*100)
            if i > 0:
                # print(li)
                # 카테고리, 작성일, 조회수, 상세url
                category = li.find('span', class_='colName').text
                r_dt = li.find('span', class_='colDate').text
                hit = li.find('span', class_='colHit').text
                a = li.find('span', class_='colSbj-cate').find_all('a')[1]  # 1 페이지 내용만 뽑아옴
                url = a.get('href')
                title = a.getText()
                seq = url.split('?')[0].split('/')[-1]
                data = {"seq": seq, "title": title, "cate": category, "hit": hit, "r_dt": r_dt, "url": url}
                cur = conn.cursor()
                cur.execute(sql, data)
                conn.commit()
                print(seq, title, category, hit, r_dt, url)

cur.close()
conn.close()
