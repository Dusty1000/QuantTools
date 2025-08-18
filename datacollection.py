import pandas
import requests
import yfinance as yf
import pandas as pd
from universe import *


#data = yf.download(sp500b,start = '2015-01-01',end = '2017-01-01',auto_adjust='true')

#print(data)


dat = []
for i in range(0, 3):
    equity = sp500a[i]

    url = 'https://financialmodelingprep.com/api/v3/financial-statement-full-as-reported/' + equity + '?period=annual&limit=50&apikey=JRNdJsE7NOTKTrNC2oxEvZlygoFxEPTM'
    r = requests.get(url)

    dat += r.json()
    print(dat)
    print(i)
pad = pd.json_normalize(dat)
print(pad.shape)
print(pad)


