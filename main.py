import sys
from interpreter.execution_engine import Evaluator


def main():
    # Check if there are enough command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python myrpal.py file_name [-ast]")
        return

    # Get the filename from the command-line arguments
    file_name = sys.argv[1]

    # Create an instance of the Evaluator class
    evaluator = Evaluator()

    # Interpret the file
    evaluator.interpret(file_name)

    # Check if the -ast switch is provided
    if len(sys.argv) >= 3 and sys.argv[2] == "-ast":
        # print the abstract syntax tree
        evaluator.print_AST()


def handle_ast_option(file_name):
    # Your code to print the abstract syntax tree
    print("Printing Abstract Syntax Tree for", file_name)


def handle_default_behavior(file_name):
    # Your code for default behavior
    print("Default behavior for", file_name)


if __name__ == "__main__":
    main()
