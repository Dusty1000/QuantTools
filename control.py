import datetime
from math import isnan

import pandas as pd

from config import *
from alphaenv import alpha,sellall,getdata
from datacollection import *

# f = open('cache.pickle','wb')
for every in allthing:
      if  isnan(every.historyRaw[0]):
         print(every.name)
# pickle.dump('allthing',f)
# f.close()
print('eeee')






for day in range(0, len(allthing[0].historyRaw)):
    for i in range(0,len(universe)):
        alpha(allthing[i].name,allthing[i].historyRaw,day,i)
sellall(len(allthing[0].historyRaw)-1)

profit,available_book = getdata()
print('e',available_book)

# 992 ench 960 ord