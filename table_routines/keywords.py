#table_routines/keywords.py

#Description
# This module contains the Keywords class that represents the keywords used in the RPAL language.

#Usage
# The Keywords class provides a set of predefined reserved words in the RPAL language.
class Keywords:
    """
    Represents the keywords used in the RPAL language.

    Keywords are predefined reserved words in the RPAL language used for various purposes.
    """

    def __init__(self):
        """
        Initializes the keywords for the RPAL language.

        Args:
            None

        Returns:
            None
        """
        # Define a set containing all the keywords in the RPAL language
        self.keywords = {
            "let",   # Used for variable declaration
            "in",    # Used for scoping
            "fn",    # Used for function definition
            "where", # Used for local definitions
            "aug",   # Augmentation operator
            "or",    # Logical OR operator
            "not",   # Logical NOT operator
            "gr",    # Greater than operator
            "ge",    # Greater than or equal to operator
            "ls",    # Less than operator
            "le",    # Less than or equal to operator
            "eq",    # Equality operator
            "ne",    # Not equal to operator
            "true",  # Boolean value for true
            "false", # Boolean value for false
            "nil",   # Empty list value
            "dummy", # Dummy value
            "within",# Used for scoping
            "and",   # Logical AND operator
            "rec"    # Used for recursive function definition
        }
