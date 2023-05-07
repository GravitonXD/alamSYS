"""
    GENERAL ABOUT: For manual running of the tasks of the preprocessor
"""
from data_collector import collector
from data_processor import process
from utils import logs_and_alerts as la


log_directory = "manual_run_logs"
def task():
    print("----------------STARTING TASK MANUALLY----------------------")
    la.Logs().success_log("Task has successfully started", log_directory)
    la.Alerts().success_alert("Task has successfully started")

    try:
        # Run data collector module
        collector.main()
        # Run trained ML model
        process.main()

        print("----------------TASK COMPLETED----------------------")
        la.Logs().success_log("Task has successfully completed", log_directory)
        la.Alerts().success_alert("Task has successfully completed")

    except:
        la.Logs().error_log("Task has failed", log_directory)
        la.Alerts().error_alert("Task has failed")


if __name__ == "__main__":
    task()
