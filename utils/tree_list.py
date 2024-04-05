# utils/list_tree.py

# Description
# This function returns an tree as a list.

# Usage
# This function takes a parse tree as input and returns an tree as a list.

def list_tree(tree):
    """
    This function takes a parse tree as input and returns an tree as a list.

    Parameters:
    tree (ParseTree): The parse tree to be traversed

    Returns:
    ast (list): The  tree as a list

    """
    ast = []

    def traverse(root, depth):
        """
        This function recursively traverses the parse tree and constructs the  tree.

        Parameters:
        root (ParseTree): The current node of the parse tree
        depth (int): The current level of indentation

        """
        #print(root)
        # Append the current node to the AST list with appropriate indentation
        ast.append("." * depth + root.data+" ")

        # Traverse each child node recursively
        for child in root.children:
            # Call traverse function for each child node with increased depth
            traverse(child, depth + 1)

    # Start traversal from the root node with depth 0
    traverse(tree, 0)

    # Return the constructed  tree
    return ast
