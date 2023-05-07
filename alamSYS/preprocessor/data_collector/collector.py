""""
    ABOUT:
        This Python Script will be used to collect historical data from the 
        Philippine Stock Market using the data provided by EODHD.

        EODHD: https://eodhistoricaldata.com/

        The data will be stored in a CSV file for further analysis.
"""


import requests
import datetime
import os
# importing modules from utils
from utils import stock_symbols as ss
from utils import logs_and_alerts as la


"""
    FUNCTION DESCRIPTION: Access the API key from the environment variable or from the API_KEY.txt file
                            Get the API key as defined from the environment variable
                            NOTE: Please define the API key in the environment variable as EOD_API_KEY
                                Otherwise create a file named "API_KEY.txt" in the tools directory and place the API key in the file
                            Get the API key from the environment variable if it exists
                            Otherwise, get the API key from the APIKey.txt file
"""
def get_API_Key():
    if os.environ.get("EOD_API_KEY") != None:
        API_KEY = os.environ.get("EOD_API_KEY")
        return API_KEY

    with open("./tools/API_KEY.txt", "r") as f:
        API_KEY = f.read()
    return API_KEY


"""
    FUNCTION DESCRIPTION: This function will return the current date in the format of YYYY-MM-DD
"""
def current_date():
    # This function will return the current date in the format of YYYY-MM-DD
    return datetime.date.today().strftime("%Y-%m-%d")


"""
    FUNCTION DESCRIPTION: This function will return the current time in the format of HH:MM:SS
"""
def log_time():
    # This function will return the current time in the format of HH:MM:SS
    return datetime.datetime.now().strftime("%H:%M:%S")



"""
    FUNCTION DESCRIPTION: This function will save the historical data in a CSV file
"""
def save_historical_data(response, file_name, stock_symbol):
    try:
        with open(file_name, "w") as f:
            f.write(response.text)

        ### LOG AND ALERT ###
        message = f"Successfully saved historical data for {stock_symbol}"
        log_directory = "data_collector_logs"
        # Log the successful data collection in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful data collection
        la.Alerts().success_alert(message)
        ######################
    except Exception as e:
        ### LOG AND ALERT ###
        message = f"Failed to save historical data for {stock_symbol}, Error Info: {e}"
        log_directory = "data_collector_logs"
        # Log the failed data collection in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed data collection
        la.Alerts().error_alert(message)
        ######################



"""
    FUNCTION DESCRIPTION: This function will get the historical data from EODHD
"""
def get_eod_data(stock_symbol, API_KEY, log_directory):
    url = f"https://eodhistoricaldata.com/api/eod/{stock_symbol}.PSE?api_token={API_KEY}&period=d" if stock_symbol != "PSEI" else f"https://eodhistoricaldata.com/api/eod/PSEI.INDX?api_token={API_KEY}&period=d"
    response = requests.get(url)
    file_name = f"/data/db/stock_data/{stock_symbol}.csv"

    if response.status_code == 200:
        ### LOG AND ALERT ###
        message = f"Successfully collected historical data for {stock_symbol}"
        # Log the successful data collection in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful data collection
        la.Alerts().success_alert(message)
        ######################

        # Save the data in a CSV file
        save_historical_data(response, file_name, stock_symbol)
    else:
        ### LOG AND ALERT ###
        message = f"Failed to collect historical data for {stock_symbol} with status code {response.status_code}"
        # Log the failed data collection in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed data collection
        la.Alerts().error_alert(message)
        ######################

    return True


def main():
    log_directory = "data_collector_logs" # Directory for the logs
    os.makedirs("/data/db/stock_data/", exist_ok=True)
    
    print("------------------- STARTING DATA COLLECTOR MODULE ---------------------\n")
    # Log the start of the data collector module
    la.Logs().success_log("Data collector module has successfully started", log_directory)
    la.Alerts().success_alert("Data collector module has successfully started")

    # Check if the API key is defined in the environment variable
    try:
        API_KEY = get_API_Key()

        ### LOG AND ALERT ###
        message = "Successfully retrieved API key"
        # Log the successful API key retrieval in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful API key retrieval
        la.Alerts().success_alert(message)
        ######################
    except Exception as e:
        ### LOG AND ALERT ###
        message = f"Failed to retrieve API key, Error Info: {e}"
        # Log the failed API key retrieval in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed API key retrieval
        la.Alerts().error_alert(message)
        ######################

        exit(1)

    try:
        # Get the list of stock symbols
        stock_symbols = ss.get_stock_symbols()
        # LOOP THROUGH THE STOCK SYMBOLS
        for stock_symbol in stock_symbols:
            retries = 0
            status = get_eod_data(stock_symbol, API_KEY, log_directory)

            # Retry if the data collection failed (max 5 retries)
            while status == False and retries < 5:
                status = get_eod_data(stock_symbol, API_KEY, log_directory)
                retries += 1
            # If the data collection failed after 5 retries, exit the program
            if status == False:
                la.Alerts().error_alert(f"Failed to collect data for {stock_symbol} after 5 retries")
                la.Logs().error_log(f"Failed to collect data for {stock_symbol} after 5 retries", log_directory)
                exit(1)
    except Exception as e:
        ### LOG AND ALERT ###
        message = f"Failed to collect data, Error Info: {e}"
        # Log the failed data collection in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed data collection
        la.Alerts().error_alert(message)
        ######################
        exit(1)
    
    
    ### LOG AND ALERT ###
    message = "Data Collector Module Finished"
    # Log the successful data collection in the success_log.txt file
    la.Logs().success_log(message, log_directory)
    # Alert the successful data collection
    la.Alerts().success_alert(message)
    ######################
    print("------------------- EXITING DATA COLLECTOR MODULE ---------------------\n")
