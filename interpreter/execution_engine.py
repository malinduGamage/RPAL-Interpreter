from lexical_analyzer.scanner import Scanner
from screener.token_screener import Screener
from parser.parser import Parser

class Evaluator:
    def __init__(self):
        """
        Initialize the Evaluator class.
        """
        # Initialize scanner, screener, and parser objects
        self.scanner = Scanner()
        self.screener = Screener()
        self.parser = Parser()

    def interpret(self, file_name):
        """
        Interpret the content of the file.

        Args:
            file_name (str): The name of the file to interpret.
        """
        try:
            # Read content from the file
            str_content = self.scanner.readFile(file_name)
            # Tokenize the content
            tokens = self.scanner.tokenScan(str_content)
            # Filter tokens
            filtered_tokens = self.screener.screener(tokens)
            # Print filtered tokens
            self.scanner.printer(filtered_tokens)
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
