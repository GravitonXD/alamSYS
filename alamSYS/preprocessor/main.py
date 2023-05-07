import schedule
import time
from data_collector import collector
from data_processor import process
from utils import init_db
from utils import logs_and_alerts as la


"""
    FUNCTION DESCRIPTION: This function will run the scheduled tasks
                            1. Run data collector module
                            2. Process the collected data
"""
def scheduled_task():
    log_directory = "scheduled_task_logs"

    print("----------------STARTING SCHEDULED TASK----------------------")
    la.Logs().success_log("Scheduled task has successfully started", log_directory)
    la.Alerts().success_alert("Scheduled task has successfully started")

    try:
        # Run data collector module
        collector.main()
        # Run trained ML model
        process.main()

        print("----------------SCHEDULED TASK COMPLETED----------------------")
        la.Logs().success_log("Scheduled task has successfully completed", log_directory)
        la.Alerts().success_alert("Scheduled task has successfully completed")

    except Exception as e:
        la.Logs().error_log(f"Scheduled task has failed. Error Info: {e}", log_directory)
        la.Alerts().error_alert(f"Scheduled task has failed. Error Info: {e}")

# Schedule every Monday to Friday at 6PM
schedule.every().monday.at("18:00").do(scheduled_task)
schedule.every().tuesday.at("18:00").do(scheduled_task)
schedule.every().wednesday.at("18:00").do(scheduled_task)
schedule.every().thursday.at("18:00").do(scheduled_task)
schedule.every().friday.at("18:00").do(scheduled_task)

log_directory = "scheduled_task_logs"
la.Logs().success_log("Initialized task schedules - Running every Monday to Friday at 6PM", log_directory)
la.Alerts().success_alert("Initialized task schedules - Running every Monday to Friday at 6PM")

try:
    la.Logs().success_log("Task Scheduler Loop has started", log_directory)
    la.Alerts().success_alert("Task Scheduler Loop has started")
    
    # initialize the database on startup
    init_db.main()

    # Run the scheduled task
    while True:
        schedule.run_pending()
        time.sleep(1)

except Exception as e:
    la.Logs().error_log(f"Scheduled task has stopped. Error Info {e}", log_directory)
    la.Alerts().error_alert(f"Scheduled task has stopped. Error Info {e}")
    