def print_AST(tree):
    """
    Prints the Abstract Syntax Tree (AST) with appropriate indentation.
    
    Args:
        tree: The root node of the AST.
    """
    def traverse(root, depth):
        """
        Recursively traverses the AST and prints each node with indentation.
        
        Args:
            root: The current node being processed.
            depth: The depth of the current node in the tree.
        """
        # Print the current node with appropriate indentation
        print("." * depth + root.data)
        
        # Recursively traverse each child node
        for child in root.children:
            traverse(child, depth + 1)

    # Start traversal from the root node with depth 0
    traverse(tree, 0)
