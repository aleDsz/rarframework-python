import sys, os

from rarframework.log_manager import LogManager


class RarFrameworkException:

    @staticmethod
    def log_error():
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        message_to_log = "Ocorreu um erro na linha %d no arquivo %s\r\n"
        message_to_log = message_to_log.format(exc_tb.tb_lineno, file_name)

        LogManager.log_error(message_to_log)