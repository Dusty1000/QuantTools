import datetime
from math import isnan
from datetime import date
from metrics import Portfolio
from alphaenv import verbose
import pandas as pd

from config import *
from alphaenv import active,sellall,getdata
from datacollection import *
period = 0
equity_count = 0

for every in allthing:
    flagged = False
    for each in every.historyRaw:
        if isnan(each):
            flagged = True
    if flagged:
        if verbose == True: print(every.name)
        allthing.remove(every)

period_max = (formatted_end_date - formatted_start_date).days
equity_max = len(allthing)

passed = False
while not passed:
    passed = True
    period= int(input('How many days to run the test for? '))
    equity_count = int(input('How many stock tickers to run over? '))
    if period > period_max:
        period = period_max
    if equity_count > equity_max:
        equity_count = equity_max
    try:
        if period in range(0,period_max+1) and equity_count in range(0,equity_max+1):
            pass
        else:
            print('Provide positive integers')
            passed = False
    except:
        print('Provide positive integers')
        passed = False





portfolio  = Portfolio()
for day in range(0, period):
    if verbose == True: print(day)
    for i in range(0,equity_count):
        active(allthing[i].name,allthing[i].historyRaw[:day+1],day,i,portfolio)
    portfolio.p_update(allthing,day)

sellall(len(allthing[0].historyRaw)-1,portfolio)
print(list(map(lambda x: round(float(x), 5), portfolio.p_report)))
print(f' You made a return of {((portfolio.p_report[-1]-1)*100):.3f} %')
portfolio.calc_daily_sharpe()
print(f' Daily sharpe_ratio was {portfolio.daily_sharpe_ratio:.4f}')
portfolio.calc_real_sharpe()
print(f' Per-trade sharpe_ratio was {portfolio.real_sharpe:.4f}')






