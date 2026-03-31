# financial-monitor

A simple Python-based financial monitoring tool that tracks stock prices and manages portfolio positions using Yahoo Finance API.

## Features

- **Stock Price Tracking**: Get real-time stock prices for any ticker
- **Portfolio Management**: Track multiple stocks with purchase prices and current values
- **Gain/Loss Calculation**: Automatically calculate gains, losses, and returns
- **Swedish Stock Support**: Full support for Nasdaq Stockholm stocks (use `.ST` suffix)
- **Portfolio Summary**: Display formatted portfolio summaries with performance metrics

## Supported Stocks

- **US Stocks**: All stocks on major US exchanges (AAPL, MSFT, GOOGL, etc.)
- **Swedish Stocks**: Nasdaq Stockholm (ERIC-B.ST, SHB-A.ST, VOLV-B.ST, etc.)
- **Global Stocks**: Most major global exchanges supported

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SerenitySensei/financial-monitor.git
cd financial-monitor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Get Stock Price

```bash
python -m src.monitor --price AAPL
python -m src.monitor --price ERIC-B.ST  # Swedish stock
```

### Display Example Portfolio

```bash
python -m src.monitor --portfolio
```

### Programmatic Usage

```python
from src.portfolio import Portfolio

# Create a portfolio
portfolio = Portfolio()

# Add stocks
portfolio.add_stock("AAPL", 10, 150.00)  # 10 shares at $150 each
portfolio.add_stock("ERIC-B.ST", 5, 75.00)  # Swedish stock

# Display portfolio
portfolio.display_portfolio()

# Get individual metrics
print(f"Portfolio Value: ${portfolio.get_portfolio_value():.2f}")
print(f"Total Gain/Loss: ${portfolio.get_portfolio_gain_loss():.2f}")
print(f"Return: {portfolio.get_portfolio_return_percent():.2f}%")
```

## Portfolio Class Methods

### Adding Stocks
```python
portfolio.add_stock(ticker, quantity, purchase_price=None)
```
- `ticker`: Stock symbol (e.g., "AAPL" or "ERIC-B.ST")
- `quantity`: Number of shares
- `purchase_price`: Cost per share (optional, fetches current price if not provided)

### Removing Stocks
```python
portfolio.remove_stock(ticker, quantity=None)
```

### Getting Information
```python
portfolio.get_current_price(ticker)           # Get current price
portfolio.get_stock_value(ticker)             # Current value of position
portfolio.get_stock_gain_loss(ticker)         # Gain/loss for position
portfolio.get_stock_return_percent(ticker)    # Return % for position
portfolio.get_portfolio_value()               # Total portfolio value
portfolio.get_total_cost()                    # Total cost basis
portfolio.get_portfolio_gain_loss()           # Total gain/loss
portfolio.get_portfolio_return_percent()      # Total return %
```

### Display
```python
portfolio.display_portfolio()      # Print formatted summary
portfolio.to_dataframe()           # Get portfolio as pandas DataFrame
```

## Swedish Stock Examples

Popular Swedish stocks on Nasdaq Stockholm:
- **ERIC-B.ST** - Ericsson
- **SHB-A.ST** - Handelsbanken
- **VOLV-B.ST** - Volvo
- **SWMA.ST** - Swedbank
- **TEL2-B.ST** - Telia Company

## Example Output

```
================================================================================
PORTFOLIO SUMMARY - 2026-03-31 15:30:45
================================================================================
Ticker    Quantity Purchase Price Current Price Total Value   Gain/Loss Return %
AAPL              5         $150.00       $175.50      $877.50      $127.50   17.00%
ERIC-B.ST         5          $75.00        $82.30      $411.50       $36.50    9.73%

--------------------------------------------------------------------------------
Total Portfolio Value:  $1,289.00
Total Cost Basis:       $1,162.50
Total Gain/Loss:        $126.50
Total Return:           10.88%
================================================================================
```

## Notes

- Stock prices are updated in real-time from Yahoo Finance
- Data for Swedish stocks may have a 15-minute delay
- The tool fetches fresh data on each call (no caching)
- For the best experience, run outside of market hours to ensure data is available

## License

See LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.