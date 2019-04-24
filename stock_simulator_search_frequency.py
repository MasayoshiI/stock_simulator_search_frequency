## =======================================================
## Masayoshi Iwasa (U14652615)
## FE 459 Spring 2019
## Assignment 12, Project 01
## 04/24/2019
## ======================================================= 


import numpy as np 
import pandas as pd 
from scipy import stats
import matplotlib.pyplot as plt

class SearchFrequencyStockSimulator:

    def __init__(self, stock_csv, searchfreq_csv, initial_capital, transaction_fee=0):
        """ Constrctor for SearchFrequencyStockSimulator class"""
        self.stock_csv = stock_csv
        self.searchfreq_csv = searchfreq_csv
        self.initial_capital = initial_capital
        self.transaction_fee = transaction_fee
        self.df = self.build_datafile()
        self.position = self.create_position()
        self.return_no_cost = self.return_no_transaction_fee()
        self.return_with_cost = self.return_with_transaction_fee(transaction_fee)

        
    
    def build_datafile(self):
        """Builds Datafile of Stock Price and Search Frequency Score"""
        df = pd.read_csv(self.stock_csv)
        df.index = df['Date']
        # copy over the Adj Close column for stock_csv:
        data = pd.DataFrame(index = df.index)
        data['Stock_Price'] = df['Adj Close']

        df = pd.read_csv(self.searchfreq_csv)
        df.index = df['Date']
    
        # copy over the Interests column for FB_interests:
        data['Interests_Score'] = df['Interests']

        return data

    def get_correlation(self):
        """Returns correlation between Stock Price and Search Frequency Score"""
        return np.corrcoef(self.df['Stock_Price'] , self.df['Interests_Score'])[0][1]

    def plot_stock_interests(self):
        """plot out Stock Price and Search Frequency Score"""
        self.df[['Stock_Price', 'Interests_Score']].plot()
        plt.show()
    
    def create_position(self):
        """Create long and short position based on the strategy"""
        position = pd.DataFrame(index=self.df.index)
        position['Position'] = None

        for i in range(len(self.df)):
       
            #over Interest score of 50
            if self.df['Interests_Score'].iloc[i] > 50:
                position['Position'].iloc[i] = 1

            # below Interest score of 50
            elif self.df['Interests_Score'].iloc[i] < 50:
                position['Position'].iloc[i] = -1
            
            # otherwise refer to the val before
            else:
                position['Position'].iloc[i] = position['Position'].iloc[i-1]    
        
        return position

    def return_no_transaction_fee(self):
        """
        The function returns a pandas.DataFrame object containing the columns 
        ['Market Return', 'Strategy Return', and 'Abnormal Return']
        This simulate without the consideration of transaction cost
        """ 
        
        # calculate the market return on the stock:
        market_return = np.log(self.df["Stock_Price"] / self.df["Stock_Price"].shift(1)) 

        strategy_return = market_return * self.position['Position'] 

        abnormal_return = strategy_return - market_return

        # make it into data frame
        d = {'Market Return' : market_return, 'Strategy Return' : strategy_return,  'Abnormal Return' : abnormal_return}
        ret = pd.DataFrame(data=d)

        return ret

    def return_with_transaction_fee(self, transaction_fee):
        """
        The function returns a pandas.DataFrame object containing the columns 
        ['Market Return', 'Strategy Return', and 'Abnormal Return']
        This simulate considers transaction cost
        """ 
        # calculate the market return on the stock:
        market_return = np.log(self.df["Stock_Price"] / self.df["Stock_Price"].shift(1)) 

        strategy_return = market_return * self.position['Position'] - transaction_fee

        abnormal_return = strategy_return - market_return

        # make it into data frame
        d = {'Market Return' : market_return, 'Strategy Return' : strategy_return,  'Abnormal Return' : abnormal_return}
        ret = pd.DataFrame(data=d)
        
        return ret

    def simulate(self, returns):
        """Simulate with given initial capital and returns data frame"""
        capital = self.initial_capital
        # Drop Nan from Data
        returns = returns.dropna()
        
        #for each reuturn add on capital
        for row in range(len(returns)):
            capital += returns["Strategy Return"].iloc[row]
            
        return capital

    def plot_cumulative_returns(self, returns):
        """Create a plot of the cumulative return for each column in the parameter returns, a pandas.DataFrame object with one or more series of returns."""
        returns.cumsum().plot()

        plt.title('Cumulative Returns')
        plt.xlabel('Date')
        plt.legend()

        plt.show()

# TEST CASE | MAIN FUNC HERE
if __name__ == "__main__":
    simulator = SearchFrequencyStockSimulator('./csv/FB_stock.csv', './csv/FB_interests.csv', 100000)
    print(simulator.get_correlation())
    # simulator.plot_stock_interests()
    # print(simulator.simulate_no_transaction_fee())
    # print(simulator.simulate_with_transaction_fee(10))
    # simulator.plot_cumulative_returns(simulator.return_no_cost)
    print(simulator.simulate(simulator.return_with_transaction_fee(10)))
    