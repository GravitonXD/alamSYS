from mongoengine import connect, disconnect
import os
from json import load
from models import Buy, Sell, Info, MlModelsInfo, StockRisksProfile
import logs_and_alerts as la


"""
    FUNCTION DESCRIPTION: Connect to the database
"""
def connect_to_db():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    try:
        connect(db=os.environ['MONGO_INITDB_DATABASE'], 
                host=os.environ['MONGO_HOST'], 
                port=int(os.environ['MONGO_PORT']))
        
        ### LOG AND ALERT ###
        message = "Successfully connected to the database"
        # Log the successful connection to the database in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful connection to the database
        la.Alerts().success_alert(message)
        ######################
    except Exception as e:
        ### LOG AND ALERT ###
        message = f"Failed to connect to the database. Error Info: {e}"
        # Log the failed connection to the database in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed connection to the database
        la.Alerts().error_alert(message)
        ######################


"""
    FUNCTION DESCRIPTION: Disconnect from the database
"""
def disconnect_from_db():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    try:
        # Disconnect from the database
        disconnect()
        
        ### LOG AND ALERT ###
        message = "Successfully disconnected from the database"
        # Log the successful disconnection from the database in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful disconnection from the database
        la.Alerts().success_alert(message)
        ######################
    except Exception as e:
        ### LOG AND ALERT ###
        message = f"Failed to disconnect from the database. Error Info: {e}"
        # Log the failed disconnection from the database in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed disconnection from the database
        la.Alerts().error_alert(message)
        ######################


"""
    FUNCTION DESCRIPTION: Reset the Buy Collection from the Database
"""
def purge_buy():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    try:
        # Delete all data in the "Buy" collection
        Buy.objects.delete()

        ### LOG AND ALERT ###
        message = "Successfully purged the Buy Collection"
        # Log the successful purging of the Buy Collection in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful purging of the Buy Collection
        la.Alerts().success_alert(message)
        ######################
    except Exception as e:
        ### LOG AND ALERT ###
        message = f"Failed to purge the Buy Collection, Error Info: {e}"
        # Log the failed purging of the Buy Collection in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed purging of the Buy Collection
        la.Alerts().error_alert(message)
        ######################


"""
    FUNCTION DESCRIPTION: Reset the Sell Collection from the Database
"""
def purge_sell():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    try:
        # Delete all data in the "Sell" collection
        Sell.objects.delete()

        ### LOG AND ALERT ###
        message = "Successfully purged the Sell Collection"
        # Log the successful purging of the Sell Collection in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful purging of the Sell Collection
        la.Alerts().success_alert(message)
        ######################
    except Exception as e:
        ### LOG AND ALERT ###
        message = f"Failed to purge the Sell Collection. Error Info: {e}"
        # Log the failed purging of the Sell Collection in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed purging of the Sell Collection
        la.Alerts().error_alert(message)
        ######################


"""
    FUNCTION DESCRIPTION: Save the data from the json file (stocks2buy) to the Buy Collection
"""
def save_buy():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    # Use the json file to save data to the "Buy" collection
    stocks2buy = load(open("/data/db/json_data/stocks2buy.json"))
    if stocks2buy != {}:
        for stock in stocks2buy:
            try:
                Buy(stock_symbol=stock, 
                    last_closing=stocks2buy[stock][0][0],
                    last_date=stocks2buy[stock][0][1], 
                    predicted_closing=stocks2buy[stock][1]).save()

                ### LOG AND ALERT ###
                message = f"Successfully saved {stock} to the Buy Collection"
                # Log the successful saving of the stock to the Buy Collection in the success_log.txt file
                la.Logs().success_log(message, log_directory)
                # Alert the successful saving of the stock to the Buy Collection
                la.Alerts().success_alert(message)
            except Exception as e:
                ### LOG AND ALERT ###
                message = f"Failed to save {stock['stock_symbol']} to the Buy Collection. Error Info: {e}"
                # Log the failed saving of the stock to the Buy Collection in the error_log.txt file
                la.Logs().error_log(message, log_directory)
                # Alert the failed saving of the stock to the Buy Collection
                la.Alerts().error_alert(message)
                # Continue to the next stock
                continue


"""
    FUNCTION DESCRIPTION: Save the data from the json file (stocks2sell) to the Sell Collection
"""
def save_sell():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    # Use the json file to save data to the "Sell" collection
    stocks2sell = load(open("/data/db/json_data/stocks2sell.json"))
    if stocks2sell != {}:
        for stock in stocks2sell:
            try:
                Sell(stock_symbol=stock, 
                    last_closing=stocks2sell[stock][0][0],
                    last_date=stocks2sell[stock][0][1], 
                    predicted_closing=stocks2sell[stock][1]).save()

                ### LOG AND ALERT ###
                message = f"Successfully saved {stock} to the Sell Collection"
                # Log the successful saving of the stock to the Sell Collection in the success_log.txt file
                la.Logs().success_log(message, log_directory)
                # Alert the successful saving of the stock to the Sell Collection
                la.Alerts().success_alert(message)
            except Exception as e:
                ### LOG AND ALERT ###
                message = f"Failed to save {stock['stock_symbol']} to the Sell Collection. Error Info: {e}"
                # Log the failed saving of the stock to the Sell Collection in the error_log.txt file
                la.Logs().error_log(message, log_directory)
                # Alert the failed saving of the stock to the Sell Collection
                la.Alerts().error_alert(message)

                # Continue to the next stock
                continue


"""
    FUNCTION DESCRIPTION: Save the data from the json file (stock_info) to the Info Collection
"""
def save_info_from_json():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    # Use the json file to save data to the "Info" collection
    json_data = load(open("/preprocessor/utils/json_data/stock_info.json"))
    for stock in json_data:
        try:
            Info(**stock).save()

            ### LOG AND ALERT ###
            message = f"Successfully saved {stock['stock_symbol']} to the Info Collection"
            # Log the successful saving of the stock to the Info Collection in the success_log.txt file
            la.Logs().success_log(message, log_directory)
            # Alert the successful saving of the stock to the Info Collection
            la.Alerts().success_alert(message)
        except Exception as e:
            ### LOG AND ALERT ###
            message = f"Failed to save {stock['stock_symbol']} to the Info Collection. Error Info: {e}"
            # Log the failed saving of the stock to the Info Collection in the error_log.txt file
            la.Logs().error_log(message, log_directory)
            # Alert the failed saving of the stock to the Info Collection
            la.Alerts().error_alert(message)

            # Continue to the next stock
            continue


"""
    FUNCTION DESCRIPTION: Save the data from the json file (model_info) to the Model_Info Collection
"""
def save_model_info_from_json():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    # Use the json file to save data to the "Model_Info" collection
    json_data = load(open("/preprocessor/utils/json_data/model_info.json"))
    for model in json_data:
        try:
            MlModelsInfo(**model).save()

            ### LOG AND ALERT ###
            message = f"Successfully saved {model['model_name']} to the Model_Info Collection"
            # Log the successful saving of the model to the Model_Info Collection in the success_log.txt file
            la.Logs().success_log(message, log_directory)
            # Alert the successful saving of the model to the Model_Info Collection
            la.Alerts().success_alert(message)
        except Exception as e:
            ### LOG AND ALERT ###
            message = f"Failed to save {model['model_name']} to the Model_Info Collection. Error Info: {e}"
            # Log the failed saving of the model to the Model_Info Collection in the error_log.txt file
            la.Logs().error_log(message, log_directory)
            # Alert the failed saving of the model to the Model_Info Collection
            la.Alerts().error_alert(message)

            # Continue to the next model
            continue


"""
    FUNCTION DESCRIPTION: Save the data from the json file (stock_risks) to the Stock Risks Collection
"""
def save_stockRisksProfile_from_json():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    # Use the json file to save data to the "Stock Risks" collection
    json_data = load(open("/preprocessor/utils/json_data/stock_risks.json"))
    for stock in json_data:
        try:
            StockRisksProfile(**stock).save()

            ### LOG AND ALERT ###
            message = f"Successfully saved {stock['stock_symbol']} to the Stock Risks Collection"
            # Log the successful saving of the stock to the Stock Risks Collection in the success_log.txt file
            la.Logs().success_log(message, log_directory)
            # Alert the successful saving of the stock to the Stock Risks Collection
            la.Alerts().success_alert(message)
        except Exception as e:
            ### LOG AND ALERT ###
            message = f"Failed to save {stock['stock_symbol']} to the Stock Risks Collection. Error Info: {e}"
            # Log the failed saving of the stock to the Stock Risks Collection in the error_log.txt file
            la.Logs().error_log(message, log_directory)
            # Alert the failed saving of the stock to the Stock Risks Collection
            la.Alerts().error_alert(message)

            # Continue to the next stock
            continue
