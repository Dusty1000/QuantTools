import datetime
from math import isnan

import pandas as pd

from config import *
from alphaenv import alpha,sellall,getdata
from datacollection import *


for every in allthing:
    flagged = False
    for i in range(0,4):
        for j in range(0,6):
            if isnan(every.financialsRaw[i][j]):
                flagged = True
    if flagged:
        print(every.name)



print('eeee')






for day in range(0, len(allthing[0].historyRaw)):
    for i in range(0,len(universe)):
        alpha(allthing[i].name,allthing[i].historyRaw,day,i)
sellall(len(allthing[0].historyRaw)-1)

profit,available_book = getdata()
print('e',available_book)

