import sqlite3
import requests
import json
conn = sqlite3.connect('stock.db')

url = 'https://api.upbit.com/v1/market/all'
res = requests.get(url)
json_data = json.loads(res.text)
print(json_data)
for row in json_data:
    print(row['market'],row['korean_name'],row['english_name'])
sql4="""insert into stock values(?,?,?)"""
cur = conn.cursor()
for row in json_data:
    cur.execute(sql4, [row['market'],row['korean_name'],row['english_name']])
conn.commit()
conn.close()
