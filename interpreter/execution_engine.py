from lexical_analyzer.scanner import Scanner
from screener.token_screener import Screener
from parser.parser_module import Parser
import utils.token_printer
import utils.AST_printer
import utils.file_handler


class Evaluator:
    def __init__(self):
        """
        Initialize the Evaluator class.
        """
        # Initialize scanner, screener, and parser objects
        self.scanner = Scanner()
        self.screener = Screener()
        self.parser = Parser()
        self.tokens = []
        self.filtered_tokens = []

    def interpret(self, file_name):
        """
        Interpret the content of the file.

        Args:
            file_name (str): The name of the file to interpret.
        """
        try:
            # Read content from the file
            str_content = utils.file_handler.read_file_content(file_name)
            # Tokenize the content
            self.tokens = self.scanner.token_scan(str_content)
            # Filter tokens
            self.filtered_tokens = self.screener.screener(self.tokens)
            # Parse the filtered tokens
            self.parser.parse(self.filtered_tokens.copy())

            if self.scanner.status == False:
                raise Exception("Scanning failed.")
            if self.parser.status == False:
                raise Exception("Parsing failed.")

        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred in {e}")

    def print_tokens(self):
        """
        Print the tokens.
        """
        if self.scanner.status:
            utils.token_printer.print_tokens(self.tokens)
        else:
            print("Scanning failed. Tokens cannot be printed.")

    def print_filtered_tokens(self):
        """
        Print the filtered tokens.
        """
        if self.scanner.status:
            utils.token_printer.print_tokens(self.filtered_tokens)
        else:
            print("Scanning failed. Filtered tokens cannot be printed.")

    def print_AST(self):
        """
        Print the Abstract Syntax Tree (AST).
        """
        if self.parser.status:
            utils.AST_printer.print_AST(self.parser.stack)
        else:
            print("Parsing failed. AST cannot be printed.")
