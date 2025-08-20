
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






