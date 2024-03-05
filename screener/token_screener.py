from lexical_analyzer.scanner import Scanner
from table_routines.keywords import Keywords
class Screener:
    def __init__(self):
        """
        Initialize the screener.
        """
        # Initialize the scanner and retrieve necessary attributes
        self.scanner = Scanner()
        self.error = self.scanner.error
        self.charMap = self.scanner.charMap
        self.fsaTable = self.scanner.fsaTable
        self.acceptStates = self.scanner.acceptStates
        # Retrieve keywords from the Keywords class
        self.keywords = Keywords().keywords

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
            if token[1] == 'DELETE' or token[1] == 'EOF':
                continue
            # Remove IDENTIFIER tokens if they match any keywords
            if token[1] == 'IDENTIFIER' and token[0] in self.keywords:
                continue
            # Add the token to the filtered list if it passes all checks
            filtered_tokens.append(token)
        
        # Return the filtered list of tokens
        return filtered_tokens
