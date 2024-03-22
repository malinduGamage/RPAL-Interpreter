import sys
from interpreter.execution_engine import Evaluator
from rpal_tests.rpal_exe import rpal_exe

def main():
    """
    Main function of the interpreter.

    Args:
        sys.argv (list): Command line arguments passed to the interpreter.

    Returns:
        None

    Raises:
        ValueError: If the number of command line arguments is less than 2.

    """

    # Check if there are enough command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python myrpal.py file_name [-ast]")
        return

    # Get the filename from the command-line arguments
    if len(sys.argv) >= 3:
        file_name = sys.argv[2]
    else:
        file_name = sys.argv[1]

    # Create an instance of the Evaluator class
    evaluator = Evaluator()

    # Interpret the file
    evaluator.interpret(file_name)

    # Check if the -ast switch is provided
    if len(sys.argv) >= 3:
        if sys.argv[1] == "-ast":
            # Print the Abstract Syntax Tree
            evaluator.print_AST()
        elif sys.argv[1] == "-t":
            # Print the tokens
            evaluator.print_tokens()
        elif sys.argv[1] == "-ft":
            # Print the filtered tokens
            evaluator.print_filtered_tokens()
        elif sys.argv[1] == "-st":
            print("Not yet implemented")
        else:
            # Default behavior: Print the Abstract Syntax Tree
            evaluator.print_AST()
    rpal_exe("div",True)    


def handle_ast_option(file_name):
    """
    Prints the Abstract Syntax Tree for the given file.

    Args:
        file_name (str): The name of the file for which the Abstract Syntax Tree is to be printed.

    Returns:
        None

    """
    # Your code to print the abstract syntax tree
    print("Printing Abstract Syntax Tree for", file_name)


def handle_default_behavior(file_name):
    """
    Prints the default behavior for the given file.

    Args:
        file_name (str): The name of the file for which the default behavior is to be printed.

    Returns:
        None

    """
    # Your code for default behavior
    print("Default behavior for", file_name)


if __name__ == "__main__":
    main()
