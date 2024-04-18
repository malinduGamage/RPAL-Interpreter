# src/error_handling/error_handler.py

# This is the main module for error handling. It provides a class ErrorHandler with static methods for handling errors.
class CseErrorHandler:
    """
    This class provides a set of static methods for handling errors.
    """
    def __init__(self, cse_machine):
        """
        This is the constructor for the ErrorHandler class. 
        """
        self.cse_machine = cse_machine

    def handle_error(self,message):
        """
        This method raises an exception with the given message.

        Args:
            message (str): The error message.
        """
        self.cse_machine._print_cse_table()
        raise Exception(message)
