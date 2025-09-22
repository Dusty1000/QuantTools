import datetime

import pandas as pd

from config import *
from alphaenv import alpha,sellall,getdata
from datacollection import *












for day in range(0, len(data)):
    for ticker in universe:
      alpha(ticker,day)
sellall(len(data)-1)

profit,available_book = getdata()
print('e',available_book)

getdata()