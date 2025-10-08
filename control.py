import datetime
from math import isnan
from modmech import transpose, determinant, inverse
import pandas as pd

from config import *
from alphaenv import alpha,sellall,getdata
from datacollection import *


for every in allthing:
    flagged = False
    for each in every.historyRaw:
        if isnan(each):
            flagged = True
    if flagged:
        print(every.name)




print('eeee')

print(inverse([   [1,3,4] ,   [7,12,7] ,  [8,0,4]   ]))


for day in range(0, 600):
    for i in range(0,325):
        alpha(allthing[i].name,allthing[i].historyRaw,day,i)

sellall(len(allthing[0].historyRaw)-1)

profit,available_book = getdata()
print('e',available_book)

