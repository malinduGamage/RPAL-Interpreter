def list_AST(tree):
    ast = []

    def traverse(root, depth):
        # Append the current node with appropriate indentation
        ast.append("." * depth + root.data)
        
        # Traverse each child node recursively
        for child in root.children:
            traverse(child, depth + 1)

    # Start traversal from the root node with depth 0
    traverse(tree, 0)
    
    #print("actual output:",ast)

    return ast
