import numpy as np
from tensorflow import keras
# importing modules from utils
from utils import stock_symbols as ss
from utils import logs_and_alerts as la


"""
    FUNCTION DESCRIPTION: This function will load the model from the /preprocessor/data_processor/ml_model directory.
                            It will try to load the model for 5 times before exiting the program.
    PARAMETERS:
        model_name: The name of the model to be loaded
        path: The path of the directory where the model is located, which is set to /preprocessor/data_processor/ml_model by default
"""
def load_model(model_name: str, path="/preprocessor/data_processor/ml_model"):
    retries = 0
    while retries < 5:
        try:
            model_path = f"{path}/{model_name}.keras"
            loaded_model = keras.models.load_model(model_path)
            return loaded_model
        except Exception as e:
            la.Alerts().error_alert(f"Failed to load model: {model_name}. Error_Info:{e}.")
            la.Logs().error_log(f"Failed to load model: {model_name}. Error_Info:{e}", "data_processor_logs")
            retries += 1
            continue
    
    # If the model failed to load after 5 retries, exit the program
    la.Alerts().error_alert(f"Failed to load model: {model_name}. Error_Info:{e}. Program will exit")
    la.Logs().error_log(f"Failed to load model: {model_name}. Error_Info:{e}", "data_processor_logs")
    exit()
        

"""
    FUNCTION DESCRIPTION: This function will allow us to iterate through stock data files
                            and predict their future movement using the loaded model.
    PARAMETERS:
        loaded_model: The loaded model that will be used to predict the future movement of the stock
        model_name: The name of the model that will be used to predict the future movement of the stock
        len_predictions: The number of predictions to be made for each stock. Default is 5.
"""
def process_data(loaded_model, model_name:str, len_predictions:int=5):
    stock_symbols = ss.get_stock_symbols()
    processed_data = {}
    window_size = loaded_model.count_params() - 1

    for stock in stock_symbols:
        closing_prices = np.genfromtxt(f'/data/db/stock_data/{stock}.csv', delimiter=',', skip_header=1, usecols=4)[(-window_size):]

        last_closing, last_date = closing_prices[-1], np.genfromtxt(f'/data/db/stock_data/{stock}.csv', delimiter=',', skip_header=1, usecols=0, dtype=str)[-1]
        last_actual = [last_closing, last_date]
        """
            PREDICTED CLOSINGS:
                1st Prediction: input[closing_prices]
                2nd Prediction: input[closing_prices[-4:], pred]
                3rd Prediction: input[closing_prices[-3:], pred]
                4th Prediction: input[closing_prices[-2:], pred]
                5th Prediction: input[closing_prices[-1:], pred]
        """
        predicted_closings = []
        for _ in range(len_predictions):
            data = np.append(closing_prices, predicted_closings)
            prediction = loaded_model.predict(data[-(window_size):].reshape(1,window_size))
            predicted_closings.append(float(prediction))

        processed_data[stock] = tuple((last_actual, {model_name: predicted_closings}))

    return processed_data
