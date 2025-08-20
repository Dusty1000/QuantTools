
import pandas
import requests
import yfinance as yf
import pandas as pd

from config import *


data = yf.download(sp500b,start = start_date,end = end_date,auto_adjust='true')

data = data['Close']

print(data['A'].loc[data.index[0]])