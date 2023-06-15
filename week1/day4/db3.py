import sqlite3
conn=sqlite3.connect('stock.db')
cur = conn.cursor()
cur.execute("""select * from stock""")
for row in cur:
    print(row)