import yfinance as yf
import matplotlib.pyplot as plt


class Stocks:
    def __init__(self,name, amount_bought, cost):
        self.amount_bought = amount_bought
        self.cost = cost
        self.name = name

class Portfolio:

    def __init__(self, stocks, cash):
        self.stocks = stocks
        self.cash = cash


data = yf.download(
    tickers='AAPL',
    start='2019-12-11',
    interval="1m"
)

data['Close'].plot()
plt.show()

print(data['Close'][-1])
