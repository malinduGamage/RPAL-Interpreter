#utils/tree_printer.py

#Description
# This module contains a function to print the tree with appropriate indentation.

#Usage
# This module provides the print_tree() function to print the AST with appropriate indentation.

from utils.tree_list import list_tree
def print_tree(tree):
    """
    Prints the Tree with appropriate indentation.
    
    Args:
        tree: The root node of the AST.
    """
    # Generate a list representation of the Tree using a depth-first traversal
    ls = list_tree(tree)
    
    # Print each node of the tree with indentation to represent the tree structure
    print("\n".join(ls))
