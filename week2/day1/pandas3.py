#pip install openpyxl
import pandas as pd
import FinanceDataReader as fdr

df = pd.read_excel("member.xlsx", sheet_name="sheet1", engine="openpyxl")
print(df.info())
for i, v in df.iterrows():
    print('=' * 100)
    print(i) #현재 for문 순서
    print('='*100)
    print(v)
    print('=' * 100)
    print(v['MEM_NAME']) #df의 특정 값만 빼오기

samsung_2022 = fdr.DataReader('005930', '2022', '2022-12-31')
print(samsung_2022.head())
# 엑셀로 내려받기
writer = pd.ExcelWriter('samsung2022.xlsx', engine='xlsxwriter')
samsung_2022.to_excel(writer, sheet_name='sheet1')
writer.close()
