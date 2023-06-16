import json
import requests
import cx_Oracle

#DB에 다음 테이블 만들어주기
# CREATE TABLE tb_stock(
#     itemCode varchar2(100)
#     ,stockName varchar2(100)
#     ,closePrice varchar2(100)
#     ,update_dt DATE DEFAULT SYSDATE
# );

sql = """INSERT INTO tb_stock(itemCode, stockName, closePrice)
            values(:1, :2, :3)"""
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
                cur = conn.cursor()
                cur.execute(sql, [val['itemCode'],val['stockName'],val['closePrice']])
                conn.commit()
                print(val['itemCode'], val['stockName'], val['closePrice'])

    conn.close()
if __name__ == '__main__':
    fn_stock_get()
