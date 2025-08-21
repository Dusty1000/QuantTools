import random
from config import *

from mechanics import *
def alpha(ticker,day):
    ran = random.random()
    if ran < 0.15:
        buy(ticker,day,random.random()/100,'long')
    elif ran > 1:
        buy(ticker, day, random.random() / 100, 'short')
    if (ran < 0.7 )& (ran > 0.3):
        sell(ticker,day)
