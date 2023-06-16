import json
import requests
import cx_Oracle

def fn_stock_get():
    conn = cx_Oracle.connect("java", "oracle", "localhost:1521/xe")
    for i in range(2):
        url="https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={0}&pageSize=50".format(str(i))
        res = requests.get(url)
        if res.status_code == 200:
            data = json.loads(res.content)
            print(data['stocks'])
            print('=' * 100)
            if len(data['stocks']) == 0:
                break
            for idx, val in enumerate(data['stocks']):
                print(val['itemCode'], val['stockName'], val['closePrice'])