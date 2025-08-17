import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """Format detailed error message with file name, line number, and error text."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] "
        f"error message [{str(error)}]"
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        self.error_message = error_message_detail(error, error_detail=error_detail)
        # Log the error immediately
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1 / 0   # force an error
    except Exception as e:
        from src.exception import CustomException
        import sys
        raise CustomException(e, sys)

