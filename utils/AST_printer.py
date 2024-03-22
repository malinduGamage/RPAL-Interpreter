from utils.AST_list import list_AST
def print_AST(tree):
    """
    Prints the Abstract Syntax Tree (AST) with appropriate indentation.
    
    Args:
        tree: The root node of the AST.
    """
    ls = list_AST(tree)
    print("\n".join(ls))
