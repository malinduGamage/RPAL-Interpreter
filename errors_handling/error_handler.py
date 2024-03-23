# error_handling/error_handler.py

# This is the main module for error handling. It provides a class ErrorHandler with static methods for handling errors.
class ErrorHandler:
    """
    This class provides a set of static methods for handling errors.
    """
    @staticmethod
    def handle_error(message):
        """
        This method raises an exception with the given message.

        Args:
            message (str): The error message.
        """
        raise Exception(message)
