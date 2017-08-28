import os, datetime, inspect


class LogManager:

    @staticmethod
    def log(log_type, log_message):
        log_file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "RarFrameworkLog.txt")
        date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        log_data = "[%s] [%s::%s] [%s] - %s\r\n"
        log_data = log_data.format(date, inspect.stack()[1][0].f_locals["self"].__class__, inspect.stack()[1][0].f_code.co_name, log_type, log_message)

        with open(log_file_name, "a") as log_file:
            log_file.write(log_data)

    @staticmethod
    def log_trace(log_message):
        LogManager.log("TRACE", log_message)

    @staticmethod
    def log_error(log_message):
        LogManager.log("ERROR", log_message)