"""
    GENERAL ABOUT: Database Document Collection Initializations upon Startup of the Docker Container
"""
import db_actions
import logs_and_alerts as la


def main():
    log_directory = "preprocessor_utils_logs/init_db" # Directory for the logs
    try:
        # Connect to the database
        db_actions.connect_to_db()

        ### LOG AND ALERT ###
        message = "Successfully connected to the database"
        # Log the successful database connection in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful database connection
        la.Alerts().success_alert(message)
        ######################
    except Exception as e:
        ### LOG AND ALERT ###
        message = f"Failed to connect to the database. Error Info: {e}"
        # Log the failed database connection in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed database connection
        la.Alerts().error_alert(message)
        ######################

        # Exit the program
        exit()

    # Initialization of Info Collection
    if db_actions.Info.objects.count() == 0:
        try:
            # Populate the Info Collection
            print("Info Collection is empty, populating...")
            db_actions.save_info_from_json()

            ### LOG AND ALERT ###
            message = "Successfully populated the Info Collection"
            # Log the successful population of the Info Collection in the success_log.txt file
            la.Logs().success_log(message, log_directory)
            # Alert the successful population of the Info Collection
            la.Alerts().success_alert(message)
            ######################
        except Exception as e:
            ### LOG AND ALERT ###
            message = f"Failed to populate the Info Collection. Error Info: {e}"
            # Log the failed population of the Info Collection in the error_log.txt file
            la.Logs().error_log(message, log_directory)
            # Alert the failed population of the Info Collection
            la.Alerts().error_alert(message)
            ######################

            # Exit the program
            exit()
    
    # Initialization of Model Info Collection
    if db_actions.MlModelsInfo.objects.count() == 0:
        try:
            # Populate the Model Info Collection
            print("Model Info Collection is empty, populating...")
            db_actions.save_model_info_from_json()

            ### LOG AND ALERT ###
            message = "Successfully populated the Model Info Collection"
            # Log the successful population of the Model Info Collection in the success_log.txt file
            la.Logs().success_log(message, log_directory)
            # Alert the successful population of the Model Info Collection
            la.Alerts().success_alert(message)
            ######################
        except Exception as e:
            ### LOG AND ALERT ###
            message = f"Failed to populate the Model Info Collection. Error Info: {e}"
            # Log the failed population of the Model Info Collection in the error_log.txt file
            la.Logs().error_log(message, log_directory)
            # Alert the failed population of the Model Info Collection
            la.Alerts().error_alert(message)
            ######################

            # Exit the program
            exit()

    # Initialization of Risks Info Collection
    if db_actions.StockRisksProfile.objects.count() == 0:
        try:
            # Populate the StockRisksProfile Collection
            print("StockRisksProfile Collection is empty, populating...")
            db_actions.save_stockRisksProfile_from_json()

            ### LOG AND ALERT ###
            message = "Successfully populated the Risks Info Collection"
            # Log the successful population of the Risks Info Collection in the success_log.txt file
            la.Logs().success_log(message, log_directory)
            # Alert the successful population of the Risks Info Collection
            la.Alerts().success_alert(message)
            ######################
        except Exception as e:
            ### LOG AND ALERT ###
            message = f"Failed to populate the Risks Info Collection. Error Info: {e}"
            # Log the failed population of the Risks Info Collection in the error_log.txt file
            la.Logs().error_log(message, log_directory)
            # Alert the failed population of the Risks Info Collection
            la.Alerts().error_alert(message)
            ######################

            # Exit the program
            exit()

    ### LOG AND ALERT ###
    message = "Successfully initialized the database"
    # Log the successful database initialization in the success_log.txt file
    la.Logs().success_log(message, log_directory)
    # Alert the successful database initialization
    la.Alerts().success_alert(message)
    ######################

    # Close the connection to the database
    db_actions.disconnect_from_db()
