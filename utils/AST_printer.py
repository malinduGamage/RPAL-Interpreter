def print_AST(stack):
    def traverse(root, n):
        print("."*n + root.data)
        if root.children:
            for child in root.children:
                traverse(child, n+1)

    if stack:
        traverse(stack.peek(), 0)
    else:
        print("Empty tree")
