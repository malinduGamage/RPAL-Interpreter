class Keywords :
    """
    Initialize the keywords for the RPAL language.

    The keywords are predefined reserved words in the RPAL language.
    """

    def __init__(self):
        """
        Initialize the keywords for the RPAL language.

        Args:
            None

        Returns:
            None
        """
        self.keywords = {
            "let", "in", "fn", "where", "aug", "or", "not", "gr", "ge", "ls",
            "le", "eq", "ne",
            "true", "false", "nil", "dummy", "within", "and", "rec"
        }