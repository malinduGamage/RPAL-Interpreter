#utils/AST_printer.py

#Description
# This module contains a function to print the Abstract Syntax Tree (AST) with appropriate indentation.

#Usage
# This module provides the print_AST() function to print the AST with appropriate indentation.

from utils.tree_list import list_tree
def print_tree(tree):
    """
    Prints the Abstract Syntax Tree (AST) with appropriate indentation.
    
    Args:
        tree: The root node of the AST.
    """
    # Generate a list representation of the Abstract Syntax Tree (AST) using a depth-first traversal
    ls = list_tree(tree)
    
    # Print each node of the AST with indentation to represent the tree structure
    print("\n".join(ls))
