import pandas as pd

from alphaenv import verbose
from datacollection import *

available_book = 1

def buy(ticker,day,size,type,i,portfolio):

    stake = portfolio.liquid*size
    portfolio.liquid -= stake
    portfolio.holdings.loc[portfolio.trade_count] = [ticker,day,stake,type,i]
    portfolio.log_book.loc[len(portfolio.log_book)] = [ticker, day, stake, type,i]
    portfolio.trade_count+=1
def sell(ticker,history,day,portfolio):
    clearer = []
    if verbose == True: print(ticker)

    for i in portfolio.holdings.index.values:
        if portfolio.holdings['equity'].loc[i] == ticker:
            if portfolio.holdings['type'].loc[i] == 'long':

                pdelta = ( history[day] / history[portfolio.holdings['date'].loc[i]] ) - 1
                value = pdelta * portfolio.holdings['size'].loc[i]

                portfolio.liquid+= value
                portfolio.return_report.append(value)
                portfolio.liquid += portfolio.holdings['size'].loc[i]
                clearer.append(i)


                if verbose == True: print(portfolio.liquid)

            if portfolio.holdings['type'].loc[i] == 'short':

                pdelta = ( history[day] / history[portfolio.holdings['date'].loc[i]] ) - 1
                value = pdelta * portfolio.holdings['size'].loc[i]

                portfolio.liquid-= value
                portfolio.return_report.append(-value)
                portfolio.liquid += portfolio.holdings['size'].loc[i]
                clearer.append(i)


                if verbose == True: print(portfolio.liquid)



    for e in clearer:
        portfolio.holdings.drop(e,inplace=True)
def sellall(day,portfolio):
    clearer = []



    for i in portfolio.holdings.index.values:
        k = portfolio.holdings['index'].loc[i]
        history = allthing[k].historyRaw
        if portfolio.holdings['type'].loc[i] == 'long':
                pdelta = ( history[day] / history[portfolio.holdings['date'].loc[i]] ) - 1
                value = pdelta * portfolio.holdings['size'].loc[i]

                portfolio.liquid += value
                portfolio.return_report.append(value)
                portfolio.liquid += portfolio.holdings['size'].loc[i]
                clearer.append(i)




        if portfolio.holdings['type'].loc[i] == 'short':
                pdelta = ( history[day] / history[portfolio.holdings['date'].loc[i]] ) - 1
                value = pdelta * portfolio.holdings['size'].loc[i]

                portfolio.liquid -= value
                portfolio.return_report.append(-value)
                portfolio.liquid += portfolio.holdings['size'].loc[i]
                clearer.append(i)



    for e in clearer:
        portfolio.holdings.drop(e, inplace=True)
def getdata():
    pass


