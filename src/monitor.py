import argparse
import sys
from src.portfolio import Portfolio
import yfinance as yf

def get_stock_price(ticker: str):
    """Fetch and display current price for a stock."""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period='1d')
        if hist.empty:
            print(f"Error: Could not find stock {ticker}")
            return
        price = hist['Close'].iloc[0]
        print(f"\n{ticker}: ${price:.2f}")
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}")

def demo_portfolio():
    """Display example portfolio with Swedish stocks."""
    print("\n" + "="*60)
    print("EXAMPLE PORTFOLIO")
    print("="*60)
    
    portfolio = Portfolio()
    
    # Add some stocks (including Swedish ones)
    stocks_to_add = [
        ("AAPL", 10),
        ("MSFT", 5),
        ("ERIC-B.ST", 20),  # Ericsson - Swedish stock
    ]
    
    print("\nAdding stocks to portfolio...")
    for ticker, shares in stocks_to_add:
        portfolio.add_stock(ticker, shares)
        price = portfolio.get_current_price(ticker)
        print(f"  {ticker}: {shares} shares @ ${price:.2f}")
    
    print("\n" + "-"*60)
    print(f"Total Portfolio Value: ${portfolio.portfolio_val():.2f}")
    print("="*60 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="Financial Monitor - Track stocks and portfolios"
    )
    parser.add_argument("--price", help="Get current price for a stock ticker")
    parser.add_argument("--portfolio", action="store_true", help="Show example portfolio")
    
    args = parser.parse_args()
    
    if args.price:
        get_stock_price(args.price)
    elif args.portfolio:
        demo_portfolio()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()