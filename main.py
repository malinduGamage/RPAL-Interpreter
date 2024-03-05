import sys
from lexical_analyzer import scanner
from screener.token_screener import Screener

def main():
    # Check if there are enough command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python myrpal.py file_name [-ast]")
        return

    # Get the filename from the command-line arguments
    file_name = sys.argv[1]

    str = scanner.readFile(file_name)
    scanner.printer(scanner.tokenScan(str))
    str = Screener.screener(str)
    print("################################################################################")
    scanner.printer(str)

    """ # Check if the -ast switch is provided
    if len(sys.argv) >= 3 and sys.argv[2] == "-ast":
        print("Abstract Syntax Tree option selected.")
        # Call a function to handle the -ast option
        handle_ast_option(file_name)
    else:
        # Call a function to handle the default behavior
        handle_default_behavior(file_name)
 """
def handle_ast_option(file_name):
    # Your code to print the abstract syntax tree
    print("Printing Abstract Syntax Tree for", file_name)

def handle_default_behavior(file_name):
    # Your code for default behavior
    print("Default behavior for", file_name)

if __name__ == "__main__":
    main()
