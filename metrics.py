import copy
import math
from alphaenv import verbose
import pandas as pd

class Portfolio():
    def __init__(self):
        self.log_book = pd.DataFrame(columns=['equity','date','size','type','index'])
        self.p_val = 0
        self.trade_count = 0
        self.p_report = []
        self.holdings =  pd.DataFrame(columns=['equity','date','size','type','index'])
        self.liquid = 1
        self.daily_sharpe_ratio = 0
        self.real_sharpe = 0
        self.return_report = []
        self.learning_rate = 0.01
    def p_update(self,allthing,day):
        clearer = []
        held_value = 0
        dummy_holdings = copy.deepcopy(self.holdings)

        for i in dummy_holdings.index.values:
            k = dummy_holdings['index'].loc[i]
            try:
                history = allthing[k].historyRaw
                if dummy_holdings['type'].loc[i] == 'long':
                    pdelta = (history[day] / history[dummy_holdings['date'].loc[i]]) - 1
                    value = pdelta * dummy_holdings['size'].loc[i]

                    held_value += value
                    held_value += dummy_holdings['size'].loc[i]
                    clearer.append(i)



                if dummy_holdings['type'].loc[i] == 'short':
                    pdelta = (history[day] / history[dummy_holdings['date'].loc[i]]) - 1
                    value = pdelta * dummy_holdings['size'].loc[i]

                    held_value -= value
                    held_value += dummy_holdings['size'].loc[i]
                    clearer.append(i)
            except:
                print(f'Broken at {i}')
        self.p_report.append(held_value + self.liquid)

    def calc_daily_sharpe(self):
        sum_of_squares = 0
        for i in self.p_report:
            sum_of_squares += i**2
        mean_of_squares = sum_of_squares / len(self.p_report)
        sum = 0
        for i in self.p_report:
            sum += i
        mean_squared = (sum/len(self.p_report))**2
        daily_variance = mean_of_squares - mean_squared
        daily_std = math.sqrt(daily_variance)
        daily_return = (self.p_report[-1] -1 ) / len(self.p_report)
        sharpe_ratio = daily_return / daily_std
        self.daily_sharpe_ratio = sharpe_ratio

    def calc_real_sharpe(self):
        sum_of_squares = 0
        for i in self.return_report:
            sum_of_squares += i ** 2
        mean_of_squares = sum_of_squares / len(self.return_report)
        sum = 0
        for i in self.return_report:
            sum += i
        mean_squared = (sum / len(self.return_report)) ** 2
        individual_variance = mean_of_squares - mean_squared
        individual_std = math.sqrt(individual_variance)
        individual_return = (self.p_report[-1]-1 )/ self.trade_count
        real_sharpe = individual_return / individual_std
        self.real_sharpe = real_sharpe

