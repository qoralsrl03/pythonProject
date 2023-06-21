#pip install xlsxwriter
import pandas as pd
import cx_Oracle
conn = cx_Oracle.connect("study", "study", "localhost:1521/xe")
df = pd.read_sql(con=conn, sql="SELECT * FROM mystore")
print(df.head())
print('=' * 100)
print(df.describe())
print('=' * 100)
writer = pd.ExcelWriter("member.xlsx", engine="xlsxwriter")
df.to_excel(writer,sheet_name="sheet1")
writer.close()
