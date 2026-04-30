from data import get_data
from analysis import calculate_returns, calculate_metrics
from visuals import plot_prices

def main():
    tickers = input('Enter stock tickers separated by commas: ')

    data = get_data(tickers)
    returns = calculate_returns(data)
    avg_returns, volatility = calculate_metrics(returns)

    print('\n--- Results ----')
    print('Average Returns: \n',(avg_returns))
    print('\nvolatility (Risk): \n', volatility)

    print('\n Best Performing Stock:', avg_returns.idxmax())
    print('Worst Performing Stock:', avg_returns.idxmin())
    print('Most Volatile Stock:', volatility.idxmax())
    print('Least Volatile Stock:', volatility.idxmin())


    plot_prices(data)
if __name__ == '__main__':
    main()