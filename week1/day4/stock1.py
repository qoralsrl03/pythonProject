# pip install -U finance-datareader
import FinanceDataReader as fdr
dk_krx = fdr.StockListing('KRX');
df_nasdaq = fdr.StockListing('NASDAQ');
print(dk_krx.head())
print(df_nasdaq.head())
samsung = fdr.DataReader('005930')
print(samsung.head())
#그래프 그려주는 라이브러리(matplotlib)
import matplotlib.pyplot as plt
#pip install matplotlib
samsung['cplse'].plot()
plt.show()