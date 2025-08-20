import datetime

import pandas as pd

from config import *
from alphaenv import *
from datacollection import *

available_book = 1

profit = 0

holdings = pd.DataFrame(columns=['equity','date','size','type'])

holdings.loc[len(holdings)] = ['A',2,0.2,'long']
print(holdings)

def buy(ticker,day,size,type):
    global available_book
    stake = available_book*size
    available_book -= stake
    holdings.loc[len(holdings)] = [ticker,day,stake,type]
def sell(ticker,day):
    global profit, available_book
    for i in range(0,len(holdings)):
        if holdings['equity'].loc[i] == ticker:
            if holdings['type'].loc[i] == 'long':

                pdelta = ( data[ticker].loc[data.index[day]] / data[ticker].loc[data.index[holdings['date'].loc[i]]] ) - 1
                value = pdelta * holdings['size'].loc[i]
                profit += value
                available_book+= value
                holdings.drop(i,inplace=True)
                print(profit)
                print(available_book)








for day in range(0, len(data)):
    for ticker in sp500a:
      alpha(ticker,day)

buy('A',34,0.1,'short')

sell('A',200)