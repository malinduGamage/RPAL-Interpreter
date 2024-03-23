from utils.AST_list import list_AST
def print_AST(tree):
    """
    Prints the Abstract Syntax Tree (AST) with appropriate indentation.
    
    Args:
        tree: The root node of the AST.
    """
    # Generate a list representation of the Abstract Syntax Tree (AST) using a depth-first traversal
    ls = list_AST(tree)
    
    # Print each node of the AST with indentation to represent the tree structure
    print("\n".join(ls))
