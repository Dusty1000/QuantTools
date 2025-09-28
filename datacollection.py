import numpy as np
import pandas
import requests
import pickle
import yfinance as yf
import pandas as pd

from config import *


class ticker:
        name = ''
        historyRaw = []
        financialsRaw = []

        def __init__(self,name,):
            self.financialsRaw = []
            self.name = name
            self.historyRaw = data[name].tolist()

            for i in range(0,4):

                    self.financialsRaw.append([yf.Ticker(name).incomestmt.iloc[:, i]['Total Revenue'],yf.Ticker(name).incomestmt.iloc[:, i]['Gross Profit'],yf.Ticker(name).incomestmt.iloc[:, i]['Cost Of Revenue'],yf.Ticker(name).incomestmt.iloc[:, i]['Research And Development'],yf.Ticker(name).cashflow.iloc[:, i]['Capital Expenditure'], yf.Ticker(name).cashflow.iloc[:, i]['Repayment Of Debt']   ])







        def history(self,day):
            return self.historyRaw[day]

        def financials(self,day,feature):
            index = findict[feature]
            return self.financialsRaw[day][index]



findict = {
    'Total Revenue' : 0,
    'Gross Profit' : 1,
    'Cost Of Revenue' : 2,
    'Research And Development' : 3,
    'Capital Expenditure' : 4,
    'Repayment Of Debt' : 5,


}
# data = yf.download(sp500b,start = start_date,end = end_date,auto_adjust='true')
# data = data['Close']
#
# everything = []
# for each in universe:
#      everything.append(ticker(each))
#      print(each)
# f = open('cache.pickle','wb')
# pickle.dump(everything,f)
# f.close()
#




f = open('cache.pickle','rb')
allthing = pickle.load(f)
f.close()
# f = open('cache.pickle','wb')
# allthing.pop()















