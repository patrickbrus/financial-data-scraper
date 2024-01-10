import yfinance as yf

def get_recent_quarter_roic(ticker):
    # Fetching data for the given ticker
    stock = yf.Ticker(ticker)

    # Getting financials
    financials = stock.financials
    balance_sheet = stock.balance_sheet

    # Extracting necessary values
    # Operating Income or EBIT (Earnings Before Interest and Taxes)
    operating_income = financials.loc['Operating Income', financials.columns[0]]

    # Total Assets and Total Liabilities
    total_assets = balance_sheet.loc['Total Assets', balance_sheet.columns[0]]
    total_liab = balance_sheet.loc['Total Liabilities Net Minority Interest', balance_sheet.columns[0]]

    # Calculate NOPAT (Net Operating Profit After Taxes)
    tax_rate = financials.loc['Tax Rate For Calcs', financials.columns[0]]  
    nopat = operating_income * (1 - tax_rate)

    # Invested Capital
    # Invested Capital = Total Assets - Excess Cash - Non-operating Assets
    # For simplicity, we'll use Total Assets - Total Liabilities
    invested_capital = total_assets - total_liab

    return nopat/invested_capital

# Example usage
tickers = ["PYPL", "PLTR", "HIMS", "CRWD", "AMZN", "MNDY", "NU", "MELI", "GOOGL", "TSLA", "CPRT", "SOFI", "KO"]

for ticker in tickers:
    try:
        roic = get_recent_quarter_roic(ticker)
        print(f"ROIC for {ticker}: {round(roic*100,2)}%")
    except:
        print(f"ROIC for {ticker} not available.")