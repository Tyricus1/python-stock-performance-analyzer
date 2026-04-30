import numpy as np

def calculate_returns(data):
    return data.pct_change().dropna()

def calculate_metrics(returns):
    avg_returns = returns.mean() * 252
    volatility = returns.std() * np.sqrt(252)
    return avg_returns, volatility