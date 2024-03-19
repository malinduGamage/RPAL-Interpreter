def print_AST(tree):
    def traverse(root, n):
        print("."*n + root.data)
        if root.children:
            for child in root.children:
                traverse(child, n+1)

    traverse(tree, 0)
