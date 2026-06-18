# tools/yahoo_finance_tool.py

import yfinance as yf

def get_financial_data(company: str):

    ticker = yf.Ticker(company)

    info = ticker.info

    return {
        "name": info.get("longName"),
        "marketCap": info.get("marketCap"),
        "trailingPE": info.get("trailingPE"),
        "revenueGrowth": info.get("revenueGrowth"),
        "profitMargins": info.get("profitMargins"),
        "debtToEquity": info.get("debtToEquity")
    }