from utils import db_actions
from utils import logs_and_alerts as la
import ml_processor as mp
import alma_processor as ap
from json import dump
from os import makedirs, path, rename
from datetime import datetime


def date_now():
    now = datetime.now()
    # date = mm-dd-yyyy
    date = now.strftime("%m-%d-%Y")
    return date

def main():
    log_directory = "data_processor_logs"

    try:
        # DEEP LEARNING MODELS TO APPLY
        model_names = ["dmd_lstm"]

        for model in model_names:
            # Load the model
            try:
                loaded_model = mp.load_model(model)
                la.Logs().success_log(f"Successfully loaded model: {model}", log_directory)
                la.Alerts().success_alert(f"Successfully loaded model: {model}")
            except Exception as e:
                la.Logs().error_log(f"Failed to load model: {model}. Error_Info:{e}", log_directory)
                la.Alerts().error_alert(f"Failed to load model: {model}. Error_Info:{e}. Program will exit")
                exit(1)
            # Process the data using the model
            try:
                processed_data = mp.process_data(loaded_model, model_name=model)
                la.Logs().success_log(f"Successfully processed data for model: {model}", log_directory)
                la.Alerts().success_alert(f"Successfully processed data for model: {model}")
            except Exception as e:
                la.Logs().error_log(f"Failed to process data for model: {model}. Error_Info:{e}", log_directory)
                la.Alerts().error_alert(f"Failed to process data for model: {model}. Error_Info:{e}. Program will exit")
                exit(1)
            # Post process the data
            try:
                stocks_to_buy, stocks_to_sell = ap.post_processing(processed_data, model)
                la.Logs().success_log(f"Successfully post processed data for model: {model}", log_directory)
                la.Alerts().success_alert(f"Successfully processed data for model: {model}")
            except Exception as e:
                la.Logs().error_log(f"Failed to post process data for model: {model}. Error_Info:{e}", log_directory)
                la.Alerts().error_alert(f"Failed to process data for model: {model}. Error_Info:{e}. Program will exit")
                exit(1)

            # Backup old stocks to buy and stocks to sell
            makedirs("/data/db/json_data", exist_ok=True)
            try:
                if path.exists("/data/db/json_data/stocks2buy.json"):
                    makedirs("/data/db/json_data/old", exist_ok=True)
                    makedirs(f"/data/db/json_data/old/{date_now()}", exist_ok=True)
                    rename("/data/db/json_data/stocks2buy.json", f"/data/db/json_data/old/{date_now()}/stocks2buy.json")
                    la.Logs().success_log(f"Successfully backed up old stocks to buy", log_directory)
                    la.Alerts().success_alert(f"Successfully backed up old stocks to buy")
                else:
                    la.Logs().success_log(f"No existing stocks2buy.json yet, this is not an error", log_directory)
                    la.Alerts().success_alert(f"No existing stocks2buy.json yet, this is not an error")
                if path.exists("/data/db/json_data/stocks2sell.json"):
                    makedirs("/data/db/json_data/old", exist_ok=True)
                    makedirs(f"/data/db/json_data/old/{date_now()}", exist_ok=True)
                    rename("/data/db/json_data/stocks2sell.json", f"/data/db/json_data/old/{date_now()}/stocks2sell.json")
                    la.Logs().success_log(f"Successfully backed up old stocks to sell", log_directory)
                    la.Alerts().success_alert(f"Successfully backed up old stocks to sell")
                else:
                    la.Logs().success_log(f"No existing stocks2sell.json yet, this is not an error", log_directory)
                    la.Alerts().success_alert(f"No existing stocks2sell.json yet, this is not an error")

            except Exception as e:
                la.Logs().error_log(f"Failed to backup old stocks to buy or sell. Error_Info:{e}", log_directory)
                la.Alerts().error_alert(f"Failed to backup old stocks to buy or sell. Error_Info:{e}")
                exit(1)

            
            # Save the stocks to buy and stocks to sell to json files in utils/json_data
            try:
                with open("/data/db/json_data/stocks2buy.json", "w") as f:
                    dump(stocks_to_buy, f)
                la.Logs().success_log(f"Successfully saved stocks to buy", log_directory)
                la.Alerts().success_alert(f"Successfully saved stocks to buy")
            except Exception as e:
                la.Logs().error_log(f"Failed to save stocks to buy or sell. Error_Info:{e}", log_directory)
                la.Alerts().error_alert(f"Failed to save stocks to buy or sell. Error_Info:{e}. Program will exit")
                exit(1)

            try:
                with open("/data/db/json_data/stocks2sell.json", "w") as f:
                    dump(stocks_to_sell, f)
                la.Logs().success_log(f"Successfully saved stocks to sell", log_directory)
                la.Alerts().success_alert(f"Successfully saved stocks to sell")
            except Exception as e:
                la.Logs().error_log(f"Failed to save stocks to buy or sell. Error_Info:{e}", log_directory)
                la.Alerts().error_alert(f"Failed to save stocks to buy or sell. Error_Info:{e}. Program will exit")
                exit(1)

    except Exception as e:
        la.Logs().error_log(f"Failed to apply machine learning model/s to collected data. Error_Info:{e}", log_directory)
        la.Alerts().error_alert(f"Failed to apply machine learning model/s to collected data. Error_Info:{e}. Program will exit")
        exit(1)

    try:
        # DATABASE ACTIONS
        db_actions.connect_to_db()
        la.Logs().success_log(f"Successfully connected to database", log_directory)
        la.Alerts().success_alert(f"Successfully connected to database")
    except Exception as e:
        la.Logs().error_log(f"Failed to connect to database. Error_Info:{e}", log_directory)
        la.Alerts().error_alert(f"Failed to connect to database. Error_Info:{e} Program will exit")
        exit(1)
    try:
        # Purge old documents from the database
        db_actions.purge_buy()
        db_actions.purge_sell()
        la.Logs().success_log(f"Successfully purged old documents from database", log_directory)
        la.Alerts().success_alert(f"Successfully purged old documents from database")
    except Exception as e:
        la.Logs().error_log(f"Failed to purge old documents from database. Error_Info:{e}", log_directory)
        la.Alerts().error_alert(f"Failed to purge old documents from database. Error_Info:{e} Program will exit")
    
    try:
        # Save the stocks to buy and stocks to sell to the database
        db_actions.save_buy()
        db_actions.save_sell()
        la.Logs().success_log(f"Successfully saved stocks to buy and sell to database", log_directory)
        la.Alerts().success_alert(f"Successfully saved stocks to buy and sell to database")
    except Exception as e:
        la.Logs().error_log(f"Failed to save stocks to buy and sell to database. Error_Info:{e}", log_directory)
        la.Alerts().error_alert(f"Failed to save stocks to buy and sell to database. Error_Info:{e} Program will exit")
        exit(1)


if __name__ == "__main__":
    main()
