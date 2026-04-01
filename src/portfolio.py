import yfinance as yf

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, ticker: str, shares: int):
        if ticker in self.stocks:
            self.stocks[ticker] += shares
        else:
            self.stocks[ticker] = shares

    def remove_stock(self, ticker: str, shares: int):
        if ticker in self.stocks:
            self.stocks[ticker] -= shares
            if self.stocks[ticker] <= 0:
                del self.stocks[ticker]

    def get_current_price(self, ticker: str):
        stock = yf.Ticker(ticker)
        return stock.history(period='1d')['Close'].iloc[0]

    def portfolio_val(self):
        total_val = 0
        for ticker, shares in self.stocks.items():
            total_val += self.get_current_price(ticker) * shares
        return total_val

    def gain_loss(self, initial_investment: float):
        current_value = self.portfolio_val()
        return current_value - initial_investment
