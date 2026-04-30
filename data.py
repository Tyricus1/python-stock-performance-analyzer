import yfinance as yf

def get_data(tickers):
    data = yf.download(tickers, period="1y")['Close']
    return data