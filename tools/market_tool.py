import yfinance as yf


def get_market_data(company):

    ticker = yf.Ticker(company)

    info = ticker.info

    return {
        "current_price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
        "fifty_two_week_low": info.get("fiftyTwoWeekLow")
    }