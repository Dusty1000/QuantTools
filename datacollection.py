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



            temp = pd.DataFrame(columns=['2024', '2023', '2022', '2021'])

            # temp.loc['Total Revenue'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Total Revenue'],
            #                             yf.Ticker('AMD').incomestmt.iloc[:, 1]['Total Revenue'],
            #                             yf.Ticker('AMD').incomestmt.iloc[:, 2]['Total Revenue'],
            #                             yf.Ticker('AMD').incomestmt.iloc[:, 3]['Total Revenue']]
            # temp.loc['Gross Profit'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Gross Profit'],
            #                            yf.Ticker('AMD').incomestmt.iloc[:, 1]['Gross Profit'],
            #                            yf.Ticker('AMD').incomestmt.iloc[:, 2]['Gross Profit'],
            #                            yf.Ticker('AMD').incomestmt.iloc[:, 3]['Gross Profit']]
            # temp.loc['Cost Of Revenue'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Cost Of Revenue'],
            #                               yf.Ticker('AMD').incomestmt.iloc[:, 1]['Cost Of Revenue'],
            #                               yf.Ticker('AMD').incomestmt.iloc[:, 2]['Cost Of Revenue'],
            #                               yf.Ticker('AMD').incomestmt.iloc[:, 3]['Cost Of Revenue']]
            # temp.loc['Research And Development'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Research And Development'],
            #                                        yf.Ticker('AMD').incomestmt.iloc[:, 1]['Research And Development'],
            #                                        yf.Ticker('AMD').incomestmt.iloc[:, 2]['Research And Development'],
            #                                        yf.Ticker('AMD').incomestmt.iloc[:, 3]['Research And Development']]
            # temp.loc['Capital Expenditure'] = [yf.Ticker('AMD').cashflow.iloc[:, 0]['Capital Expenditure'],
            #                                   yf.Ticker('AMD').cashflow.iloc[:, 1]['Capital Expenditure'],
            #                                   yf.Ticker('AMD').cashflow.iloc[:, 2]['Capital Expenditure'],
            #                                   yf.Ticker('AMD').cashflow.iloc[:, 3]['Capital Expenditure']]
            # temp.loc['Repayment Of Debt'] = [yf.Ticker('AMD').cashflow.iloc[:, 0]['Repayment Of Debt'],
            #                                 yf.Ticker('AMD').cashflow.iloc[:, 1]['Repayment Of Debt'],
            #                                 yf.Ticker('AMD').cashflow.iloc[:, 2]['Repayment Of Debt'],
            #                                 yf.Ticker('AMD').cashflow.iloc[:, 3]['Repayment Of Debt']]





        def history(self,day):
            return self.historyRaw[day]

        def financials(self,day,feature):
            index = findict[feature]
            return self.financialsRaw[day][index]

data = yf.download(sp500b,start = start_date,end = end_date,auto_adjust='true')

data = data['Close']

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
amd.loc['Cost Of Revenue'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Cost Of Revenue'],yf.Ticker('AMD').incomestmt.iloc[:, 1]['Cost Of Revenue'],yf.Ticker('AMD').incomestmt.iloc[:, 2]['Cost Of Revenue'],yf.Ticker('AMD').incomestmt.iloc[:, 3]['Cost Of Revenue']    ]
amd.loc['Research And Development'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Research And Development'],yf.Ticker('AMD').incomestmt.iloc[:, 1]['Research And Development'],yf.Ticker('AMD').incomestmt.iloc[:, 2]['Research And Development'],yf.Ticker('AMD').incomestmt.iloc[:, 3]['Research And Development']    ]
amd.loc['Capital Expenditure'] = [yf.Ticker('AMD').cashflow.iloc[:,0]['Capital Expenditure'],yf.Ticker('AMD').cashflow.iloc[:,1]['Capital Expenditure'],yf.Ticker('AMD').cashflow.iloc[:,2]['Capital Expenditure'],yf.Ticker('AMD').cashflow.iloc[:,3]['Capital Expenditure']]
amd.loc['Repayment Of Debt'] = [yf.Ticker('AMD').cashflow.iloc[:,0]['Repayment Of Debt'],yf.Ticker('AMD').cashflow.iloc[:,1]['Repayment Of Debt'],yf.Ticker('AMD').cashflow.iloc[:,2]['Repayment Of Debt'],yf.Ticker('AMD').cashflow.iloc[:,3]['Repayment Of Debt']]

print(yf.Ticker('AMD').cashflow)
a = yf.Ticker('AMD').cashflow
a.to_csv('store.csv')
print(amd)

#for tickero in universe:
        # amd.loc['Total Revenue'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Total Revenue'],
        #                             yf.Ticker('AMD').incomestmt.iloc[:, 1]['Total Revenue'],
        #                             yf.Ticker('AMD').incomestmt.iloc[:, 2]['Total Revenue'],
        #                             yf.Ticker('AMD').incomestmt.iloc[:, 3]['Total Revenue']]
        # amd.loc['Gross Profit'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Gross Profit'],
        #                            yf.Ticker('AMD').incomestmt.iloc[:, 1]['Gross Profit'],
        #                            yf.Ticker('AMD').incomestmt.iloc[:, 2]['Gross Profit'],
        #                            yf.Ticker('AMD').incomestmt.iloc[:, 3]['Gross Profit']]
        # amd.loc['Cost Of Revenue'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Cost Of Revenue'],
        #                               yf.Ticker('AMD').incomestmt.iloc[:, 1]['Cost Of Revenue'],
        #                               yf.Ticker('AMD').incomestmt.iloc[:, 2]['Cost Of Revenue'],
        #                               yf.Ticker('AMD').incomestmt.iloc[:, 3]['Cost Of Revenue']]
        # amd.loc['Research And Development'] = [yf.Ticker('AMD').incomestmt.iloc[:, 0]['Research And Development'],
        #                                        yf.Ticker('AMD').incomestmt.iloc[:, 1]['Research And Development'],
        #                                        yf.Ticker('AMD').incomestmt.iloc[:, 2]['Research And Development'],
        #                                        yf.Ticker('AMD').incomestmt.iloc[:, 3]['Research And Development']]
        # amd.loc['Capital Expenditure'] = [yf.Ticker('AMD').cashflow.iloc[:, 0]['Capital Expenditure'],
        #                                   yf.Ticker('AMD').cashflow.iloc[:, 1]['Capital Expenditure'],
        #                                   yf.Ticker('AMD').cashflow.iloc[:, 2]['Capital Expenditure'],
        #                                   yf.Ticker('AMD').cashflow.iloc[:, 3]['Capital Expenditure']]
        # amd.loc['Repayment Of Debt'] = [yf.Ticker('AMD').cashflow.iloc[:, 0]['Repayment Of Debt'],
        #                                 yf.Ticker('AMD').cashflow.iloc[:, 1]['Repayment Of Debt'],
        #                                 yf.Ticker('AMD').cashflow.iloc[:, 2]['Repayment Of Debt'],
        #                                 yf.Ticker('AMD').cashflow.iloc[:, 3]['Repayment Of Debt']]
findict = {
    'Total Revenue' : 0,
    'Gross Profit' : 1,
    'Cost Of Revenue' : 2,
    'Research And Development' : 3,
    'Capital Expenditure' : 4,
    'Repayment Of Debt' : 5,

}

print(yf.Ticker('ABBV'))
tracker = 0
everything = []
#for each in universe:
    #everything.append(ticker(each))
print(tracker)
#f = open('cache.pickle','wb')
#pickle.dump(everything,f)
#f.close()
f = open('cache.pickle','rb')
allthing = pickle.load(f)
f.close()


input()













