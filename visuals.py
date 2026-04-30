import matplotlib.pyplot as plt

def plot_prices(data):
    data.plot(figsize=(10,5))
    plt.title('Stock Price Trends')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()