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
            handle_ast_option(evaluator)
        elif sys.argv[1] == "-t":
            # Print the tokens
            handle_tokens_option(evaluator)
        elif sys.argv[1] == "-ft":
            # Print the filtered tokens
            handle_filtered_tokens_option(evaluator)
        elif sys.argv[1] == "-st":
            # Print the standard tree
            #handle_standard_tree_option(evaluator)
            print("Not yet implemented")
        elif sys.argv[1] == "-r":
            # Print the original RPAL evaluation(file should be in rpal_test/rpal_source file)
            try :
                handle_original_rpal_eval()
            except :
                print("Error in original RPAL evaluation\n(file should be in rpal_test/rpal_source file)")
        elif sys.argv[1] == "-rast":
            # Print the original RPAL evaluation(file should be in rpal_test/rpal_source file)
            try :
                handle_original_rpal_ast()
            except :
                print("Error in original RPAL evaluation\n(file should be in rpal_test/rpal_source file)")

        else:
            # Default behavior: Evaluate the program
            #handle_default_behavior(evaluator)
            print("Not yet implemented")
   


def handle_ast_option(evaluator):
    """
    Prints the Abstract Syntax Tree for the given file.

    Args:
        evaluator (Evaluator): An instance of the Evaluator class.

    Returns:
        None

    """
    # Your code to print the abstract syntax tree
    evaluator.print_AST()

def handle_standard_tree_option(evaluator):
    """
    Prints the Standard Tree for the given file.

    Args:
        evaluator (Evaluator): An instance of the Evaluator class.

    Returns:
        None

    """
    # Your code to print the standard tree
    evaluator.print_standard_tree()

def handle_default_behavior(evaluator):
    """
    Prints the default behavior for the given file.

    Args:
        evaluator (Evaluator): An instance of the Evaluator class.

    Returns:
        None

    """
    # Your code for default behavior
    print("Not yet implemented")

def handle_tokens_option(evaluator):
    """
    Prints the tokens for the given file.

    Args:
        evaluator (Evaluator): An instance of the Evaluator class.

    Returns:
        None

    """
    # Your code to print the tokens
    evaluator.print_tokens()

def handle_filtered_tokens_option(evaluator):
    """
    Prints the filtered tokens for the given file.

    Args:
        evaluator (Evaluator): An instance of the Evaluator class.

    Returns:
        None

    """
    # Your code to print the filtered tokens
    evaluator.print_filtered_tokens()

def handle_original_rpal_eval(file_name):
    """
    Handles the original RPAL evaluation.

    Args:
        None

    Returns:
        None

    """
    # Your code to handle the original RPAL evaluation
    rpal_exe(file_name)

def handle_original_rpal_ast(file_name):
    """
    Handles the original RPAL evaluation.

    Args:
        None

    Returns:
        None

    """
    # Your code to handle the original RPAL evaluation
    rpal_exe(file_name, True)

if __name__ == "__main__":
    main()
