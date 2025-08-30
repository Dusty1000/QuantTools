import numpy as np
import pandas
import requests
import yfinance as yf
import pandas as pd

from config import *


#data = yf.download(sp500b,start = start_date,end = end_date,auto_adjust='true')

#data = data['Close']

#print(data['A'].loc[data.index[0]])
sto = pd.DataFrame([yf.Ticker('EBAY').cashflow['2024-12-31'] , yf.Ticker('EBAY').financials['2024-12-31']])


sto.to_csv('store.csv')
print(sto['Total Revenue'])

print(yf.Ticker('AMD').incomestmt)


#for ticker in universe:
 #   for i in range(0,4):
  #      try:
   #          print(ticker,' ,',i, ',', yf.Ticker(ticker).incomestmt.iloc[:, i]['Total Revenue'])
    #    except:
     #       print('stop',ticker)
#print('ez')



amd = pd.DataFrame(columns=['2024','2023','2022','2021'])
amd.loc['Total Revenue'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Total Revenue'],yf.Ticker('AMD').incomestmt.iloc[:, 1]['Total Revenue'],yf.Ticker('AMD').incomestmt.iloc[:, 2]['Total Revenue'],yf.Ticker('AMD').incomestmt.iloc[:, 3]['Total Revenue']    ]
amd.loc['Gross Profit'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Gross Profit'],yf.Ticker('AMD').incomestmt.iloc[:, 1]['Gross Profit'],yf.Ticker('AMD').incomestmt.iloc[:, 2]['Gross Profit'],yf.Ticker('AMD').incomestmt.iloc[:, 3]['Gross Profit']    ]
print(amd)

#im so fucking lost, all i did was add the error flag now it doesnt even have errors