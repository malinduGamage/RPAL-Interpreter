#screener/token_screener.py

#Description
#This module contains the Screener class, which is responsible for filtering unwanted tokens from the input list of tokens.

#Usage
#The Screener class provides the screener() method, which removes unwanted tokens from the input list of tokens and returns the filtered list.

from table_routines.keywords import Keywords
from utils.tokens import Token

class Screener:
    """
    Token Screener class responsible for filtering unwanted tokens from the input list of tokens.

    Attributes:
        keywords (set): Set containing keywords to be filtered out from the token list.

    Methods:
        screener(tokens): Removes unwanted tokens from the input list of tokens and returns the filtered list.
    """
    def __init__(self):
        """
        Initialize the screener.

        Args:
            None

        Returns:
            None

        """
        # Retrieve keywords from the Keywords class
        self.keywords = Keywords().keywords

    # Method to filter unwanted tokens from the input list of tokens
    def screener(self, tokens):
        """
        Remove unwanted tokens from the input list of tokens.

        Args:
            tokens (list): List of tokens to be screened.

        Returns:
            list: Filtered list of tokens.
        """
        # Iterate through the tokens
        filtered_tokens = []
        for token in tokens:
            # Remove tokens marked for deletion or EOF tokens
            if token.get_type() == 'DELETE':
                continue
            # Remove IDENTIFIER tokens if they match any keywords
            elif token.get_type() == 'ID' and token.get_value() in self.keywords:
                filtered_tokens.append(Token(token.get_value(), "KEYWORD"))
            # Add the token to the filtered list if it passes all checks
            else:
                filtered_tokens.append(token)
        # Add an EOF token to the end of the filtered list
        filtered_tokens.append(Token("EOF", "EOF"))
        # Return the filtered list of tokens
        return filtered_tokens
