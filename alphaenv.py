import math
import random
from config import *

from mechanics import *


def alpha(ticker, history, day, i):

    if day > 0:
        change = ((history[day] - history[day - 1]) / history[day - 1])
        #direction = -1 * 1 / 2 * math.log((1 + change) / (1 - change), math.e)
        #direction = -((math.e)**change+(math.e)**-change)/((math.e)**change-(math.e)**-change)
        direction = - change
        if direction > 0:
            buy(ticker,day,direction/8,'long',i)
        else:
            buy(ticker,day,-direction/24,'short',i)

        sell(ticker,history,day+1)




# def alpha(ticker,history,day,i):
#     ran = random.random()
#     if ran < 0.15:
#         buy(ticker,day,random.random()/100,'long',i)
#     elif ran > 1:
#         buy(ticker, day, random.random() / 100, 'short',i)
#     if (ran < 0.7 )& (ran > 0.3):
#         sell(ticker,history,day)

