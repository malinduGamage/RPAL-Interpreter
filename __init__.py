#__init__.py

"""
RPAL Interpreter package providing tools for parsing and interpreting RPAL programs.
"""

# Description:
# The RPAL Interpreter package offers a comprehensive set of tools for parsing and interpreting RPAL (Recursive Porgramming Algorithmic Language) programs. It comprises modules for lexical analysis, parsing, and execution, along with utilities for error handling and token manipulation.

# The core functionalities of the RPAL Interpreter package include:
# - Lexical Analysis: Modules for scanning input strings and generating tokens.
# - Parsing: Modules for constructing Abstract Syntax Trees (ASTs) from token streams.
# - Execution: Modules for interpreting RPAL programs by traversing ASTs and executing corresponding operations.
# - Error Handling: Utilities for detecting and handling errors during scanning, parsing, and execution.

# Usage:
# 1. Import the necessary modules from the RPAL Interpreter package.
# 2. Use the provided classes and methods to perform lexical analysis, parsing, and execution of RPAL programs.
# 3. Handle errors using the provided error handling utilities.

# Example:
# ```
# from rpal_interpreter.lexical_analyzer import Scanner
# from rpal_interpreter.parser import Parser
# from rpal_interpreter.execution_engine import Evaluator
# from rpal_interpreter.errors_handling import ErrorHandler
# from rpal_interpreter.utils.tokens import Token
# from rpal_interpreter.utils.node import Node
# from rpal_interpreter.utils.stack import Stack
# from rpal_interpreter.utils.file_handler import read_file_content
# from rpal_interpreter.table_routines.keywords import Keywords
#
# # Perform lexical analysis
# scanner = Scanner()
# tokens = scanner.token_scan("let x = 5 in x + 1;")
#
# # Perform parsing
# parser = Parser()
# parser.parse(tokens)
# parse_tree = parser.get_parse_tree()
#
# # Perform execution
# evaluator = Evaluator()
# evaluator.interpret("example.rpal")
# evaluator.print_tokens()
# evaluator.print_filtered_tokens()
# evaluator.print_AST()
#
# # Handle errors
# ErrorHandler.handle_error("An error occurred.")
# ```

# Note:
# - Replace `"example.rpal"` with the actual name of the RPAL file to be interpreted.
# - Ensure that the RPAL file exists in the specified location.
# - Handle errors appropriately using the provided error handling utilities.

