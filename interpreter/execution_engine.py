#interpreter/execution_engine.py

# Description:
# This module serves as the main execution engine of the RPAL interpreter. It coordinates the interpretation process, including tokenization, filtering, parsing, and printing of tokens, filtered tokens, and the Abstract Syntax Tree (AST) of the program.

# Usage:
# The Evaluator class in this module provides methods to interpret RPAL programs and print their corresponding tokens, filtered tokens, and AST.
# To use the Evaluator, create an instance of the Evaluator class.
# Call the interpret() method with the name of the RPAL file to be interpreted.
# Call the print_tokens(), print_filtered_tokens(), or print_AST() methods to print the tokens, filtered tokens, or AST, respectively.
# If parsing fails due to invalid RPAL syntax, the interpreter will print an error message indicating the failure.
# If scanning fails due to invalid characters or tokens, the interpreter will raise a ScannerError.
# If the RPAL file is not found, the interpreter will print a corresponding error message.

from lexical_analyzer.scanner import Scanner
from screener.token_screener import Screener
from parser.parser_module import Parser
import utils.token_printer
import utils.AST_list
import utils.AST_printer
import utils.file_handler


class Evaluator:
    """
    The Evaluator class interprets RPAL programs.

    Attributes:
        scanner (Scanner): An instance of the Scanner class for tokenization.
        screener (Screener): An instance of the Screener class for token filtering.
        parser (Parser): An instance of the Parser class for parsing.
        tokens (list): A list to store tokens generated from the input file.
        filtered_tokens (list): A list to store filtered tokens after screening.
        parse_tree (Node): The root node of the parse tree representing the program's Abstract Syntax Tree (AST).
    """
    def __init__(self):
        """
        Initialize the Evaluator class.
        """
        # Initialize scanner, screener, and parser objects
        
        self.scanner = Scanner()       # Initialize the scanner object
        self.screener = Screener()     # Initialize the screener object
        self.parser = Parser()         # Initialize the parser object
        self.tokens = []               # Initialize a list to store tokens
        self.filtered_tokens = []      # Initialize a list to store filtered tokens
        self.parse_tree = None         # Initialize the parse tree

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

            self.parse_tree = self.parser.stack.peek()

        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred in {e}")
            if self.scanner.status == False:
                print("Scanning failed.")
            elif self.parser.status == False:
                print("Parsing failed.")

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
        Prints the Abstract Syntax Tree (AST) of the program.

        Raises:
            ValueError: If the AST is not available.

        Returns:
            None: If the AST is printed.
        """
        if self.parser.status:
            utils.AST_printer.print_AST(self.parse_tree)
        else:
            print("AST cannot be printed.")

    def get_ast_list(self):
        """
        Retrieves the abstract syntax tree (AST) list representation.

        Returns:
            list: AST list representation.
        """
        # Check if parsing was successful
        if self.parser.status:
            # Call the list_AST function to generate AST list
            return utils.AST_list.list_AST(self.parse_tree)
        else:
            # Print a message indicating that AST cannot be printed
            return []
