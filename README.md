# Trading Strategy: Search Frequency Method

This Strategy uses Google trends's serach frequency score to determine weather to buy or sell a stock.
The score ranged from 0 to 100, 0 being no data found and 100 being the peak popularity for the term. Simulator decides to buy when score > 50 and sells when score < 50, when the score is 50 follows the previous week.
Due to the fact that Search Frequency Score is visible by weekly bases historical prices data also is weekly instead of daily.

## Author

Masayoshi Iwasa (miwasa20@bu.edu)

## Getting Started / Explanation for each function

Create SearchFrequencyStockSimulator class using csv files, initial capital, and transaction fee.

- build_datafile function makes pandas data frame of Stock Price and Search Frequency Score

- get_correlation function returns correlation between Stock Price and Search Frequency Score

- plot_stock_interests plots out Stock Price and Search Frequency Score

- create_position create long and short position based on the strategy

- return_no_transaction_fee function returns a pandas.DataFrame object containing the columns ['Market Return', 'Strategy Return', and 'Abnormal Return'] This simulate without the consideration of transaction cost

- return_with_transaction_fee function returns a pandas.DataFrame object containing the columns ['Market Return', 'Strategy Return', and 'Abnormal Return'] This simulate considers transaction cost

- simulate function simulates with given initial capital and returns data frame from the class

- plot_cumulative_returns create a plot of the cumulative return for each column in the parameter returns, a pandas.DataFrame object with one or more series of returns.

### Prerequisites

Python 3
pandas ver 0.24.2
scypy ver 1.0.0
numpy ver 1.13.3
matplotlib ver 2.1.1

Stock CSV File (Weekly)
Google Trends Search Frequency Score CSV File

### Assumptions

1 You may make any reasonable assumptions, but your must document them clearly. Here are some baseline assumptions that you may make for this assignment without additional documentation:
2 You may buy fractional shares as needed.
3 No restrictions on short-selling and no margin requirements.
4 No taxes.
5 Trading fees or commissions: make your calculations two ways: once, without trading fees or commissions, and again with EITHER a fixed $10 commission per trade, or else a 0.25% trading fee (i.e., the bid-ask spread)time you buy or sell.
6 You may NOT assume a time-machine (i.e., you cannot look at the returns and then go back and buy the stocks that will perform well).

### Conclusion

This method can only work for weekly trading due to the fact that google trends only shows weekly search frequency data.
Relying on the search frequency score might not be the best strategy since the search frequency score's range is very limited (0-100), which does not makes the strategy specific enough to make decision.
