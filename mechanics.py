import pandas as pd
from datacollection import *

available_book = 1

profit = 0
tot = 0
holdings = pd.DataFrame(columns=['equity','date','size','type','index'])
log_book = pd.DataFrame(columns=['equity','date','size','type','index'])

def buy(ticker,day,size,type,i):
    global available_book,tot
    stake = available_book*size
    available_book -= stake
    holdings.loc[tot] = [ticker,day,stake,type,i]
    log_book.loc[len(log_book)] = [ticker, day, stake, type,i]
    tot+=1
def sell(ticker,history,day):
    clearer = []
    print(ticker)
    global profit, available_book,tot
    for i in holdings.index.values:
        if holdings['equity'].loc[i] == ticker:
            if holdings['type'].loc[i] == 'long':

                pdelta = ( history[day] / history[holdings['date'].loc[i]] ) - 1
                value = pdelta * holdings['size'].loc[i]
                profit += value
                available_book+= value
                available_book += holdings['size'].loc[i]
                clearer.append(i)

                print(profit)
                print(available_book)

            if holdings['type'].loc[i] == 'short':

                pdelta = ( history[day] / history[holdings['date'].loc[i]] ) - 1
                value = pdelta * holdings['size'].loc[i]
                profit -= value
                available_book-= value
                available_book += holdings['size'].loc[i]
                clearer.append(i)

                print(profit)
                print(available_book)



    for e in clearer:
        holdings.drop(e,inplace=True)
def sellall(day):
    clearer = []

    global profit, available_book, tot
    for i in holdings.index.values:
        history = allthing[i].historyRaw
        if holdings['type'].loc[i] == 'long':
                pdelta = ( history[day] / history[holdings['date'].loc[i]] ) - 1
                value = pdelta * holdings['size'].loc[i]
                profit += value
                available_book += value
                available_book += holdings['size'].loc[i]
                clearer.append(i)

                print(profit)
                print(available_book)

        if holdings['type'].loc[i] == 'short':
                pdelta = ( history[day] / history[holdings['date'].loc[i]] ) - 1
                value = pdelta * holdings['size'].loc[i]
                profit -= value
                available_book -= value
                available_book += holdings['size'].loc[i]
                clearer.append(i)

                print(profit)


    for e in clearer:
        holdings.drop(e, inplace=True)
def getdata():
    return profit,available_book


