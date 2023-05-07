import numpy as np
from utils import stock_symbols as ss


"""
    FUNCTION DESCRIPTION: Computes for the Arnaud Legoux Moving Average (ALMA) of a stock market closing prices
                            Formula: 1/(sigma * sqrt(2 * pi)) * exp(-(x - offset * (window_size - 1))^2 / (2 * sigma^2))
    PARAMETERS:
        data: a list of closing prices
        window_size: the number of days to use in the moving average
        sigma: the standard deviation of the Gaussian window
        offset: the offset of the Gaussian window
"""
def alma(data, window_size:int, sigma:float, offset:float):
    m = offset * (window_size - 1)
    s = window_size / sigma
    w = np.exp(-(np.arange(window_size) - m)**2 / (2 * s**2))
    w /= w.sum()
    return np.convolve(data, w, mode='valid')


"""
    FUNCTION DESCRIPTION: This function will determine if the stock should be bought or sold using a entry and exit strategy
                            Entry Strategy: If the slow ALMA is greater than the fast ALMA, then buy the stock
                            Exit Strategy: If the fast ALMA is greater than the slow ALMA, then sell the stock
    PARAMETERS:
        slow_alma: a list of values that represents the slow ALMA
        fast_alma: a list of values that represents the fast ALMA
        closing_prices: a list of closing prices
"""
def back_tracking(slow_alma, fast_alma, closing_prices):
    # Initialize a position variable to determine if the stock should be bought or sold
    # 0 = None, 1 = Buy, and -1 = Sell
    position = 0
    entry_flag = False
    exit_flag = False

    for i, j, k in zip(slow_alma, fast_alma, closing_prices):
        if i > j and position == 0 or position == -1:
            position = 1
            entry_flag = True
        elif i < j and position == 0 or position == 1:
            position = -1
            exit_flag = True

        if entry_flag:
            entry_price = k
            entry_flag = False
        if exit_flag:
            exit_price = k
            exit_flag = False

    return position


""" 
    FUNCTION DESCRIPTION: Post processing of processed data (predicted stock prices) 
                            to determine which stocks to buy and sell
                            based on the back_tracking function.
    PARAMETERS:
        processed_data: a dictionary of the processed data
        model_name: the name of the model used to process the data
"""
def post_processing(processed_data, model_name:str):
    stock_symbols = ss.get_stock_symbols()
    
    # Initialize the dictionaries for the stocks to buy and stocks to sell
    stocks_to_buy = {}
    stocks_to_sell = {}

    # Iterate through the stock symbols

    for stock in stock_symbols:
        # Get the last 200 days of closing prices of the stock
        closing_prices = np.genfromtxt(f'/data/db/stock_data/{stock}.csv',
                                        delimiter=',',
                                        skip_header=1,
                                        usecols=4)
        closing_prices = closing_prices[-200:]
        # Append the 5 predicted closing prices to the closing prices
        closing_prices = np.append(closing_prices, processed_data[stock][1][model_name])
        # Compute for the slow and fast ALMA
        slow_alma = alma(closing_prices, 10, 17, 0.95)
        fast_alma = alma(closing_prices, 6, 13, 0.85)

        if back_tracking(slow_alma, fast_alma, closing_prices) == 1:
            stocks_to_buy[stock] = processed_data[stock]
        elif back_tracking(slow_alma, fast_alma, closing_prices) == -1:
            stocks_to_sell[stock] = processed_data[stock]

        
    return stocks_to_buy, stocks_to_sell
