import datetime
from os import path
from os import makedirs


"""
    CLASS DESCRIPTION: A class that logs messages, either success or error to a file in the specified logs directory
"""
class Logs:
    """
        FUNCTION DESCRIPTION: The constructor for the Logs class
    """
    def __init__(self):
        self.logs, self.date, self.time = "", datetime.date.today().strftime("%Y-%m-%d"), datetime.datetime.now().strftime("%H:%M:%S")
    

    """
        FUNCTION DESCRIPTION: This function will log a success message to a file in the specified logs directory
    """
    def success_log(self, message, log_directory):
        makedirs(f"/data/db/{log_directory}/", exist_ok=True)
        self.logs = f"{self.date}, {self.time}, {message}\n"
        action = "a" if path.exists(f"/data/db/{log_directory}/success_log.csv") else "w"
        with open(f"/data/db/{log_directory}/success_log.csv", action) as success_log:
            success_log.write(self.logs)
    

    """
        FUNCTION DESCRIPTION: This function will log an error message to a file in the specified logs directory
    """
    def error_log(self, message, log_directory):
        makedirs(f"/data/db/{log_directory}/", exist_ok=True)
        self.logs = f"{self.date}, {self.time}, {message}\n"
        action = "a" if path.exists(f"/data/db/{log_directory}/error_log.csv") else "w"
        with open(f"/data/db/{log_directory}/error_log.csv", action) as error_log:
            error_log.write(self.logs)


"""
    CLASS DESCRIPTION: A class that alerts messages, either success or error to the console.
                        This class inherits from the Logs class
"""
class Alerts(Logs):
    """
        FUNCTION DESCRIPTION: The constructor for the Alerts class
    """
    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()
    

    """
        FUNCTION DESCRIPTION: This function will alert a success message to the console
    """
    def success_alert(self, message):
        print(f" \033[1;32m [SUCCESS] \033[m{self.date} {self.time} : {message}")
    

    """
        FUNCTION DESCRIPTION: This function will alert an error message to the console
    """
    def error_alert(self, message):
        print(f" \033[1;31m [ERROR] \033[m{self.date} {self.time} : {message}")



