import sqlite3
# 일회성 사용 : memory:
# 파일명입력 (파일생성)
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('stock.db')
# 테이블 생성
cur = conn.cursor()
sql = """
    create table stock(
        code varchar2(100)
        ,kor_nm varchar2(100)
        ,en_nm varchar2(100)
    )
"""

cur.execute(sql)