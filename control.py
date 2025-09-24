import datetime

import pandas as pd

from config import *
from alphaenv import alpha,sellall,getdata
from datacollection import *












for day in range(0, len(data)):
    for i in range(0,len(universe)):
        alpha(allthing[i].name,allthing[i].historyRaw,day,i)
sellall(len(data)-1)

profit,available_book = getdata()
print('e',available_book)

