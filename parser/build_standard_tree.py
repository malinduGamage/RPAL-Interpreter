
from utils.node import Node


class standard_tree:
    def __init__(self, tree):
        self.tree = tree
        self.standard_tree = None
        self.status = False

    def build_standard_tree(self):
        tree = self.tree
        if tree.data == "let":
            tree.data = "gamma"
            tree.children[0].data = "lambda"
            p = tree.children[1]
            tree.children[1] = tree.children[0].children[1]
            tree.children[0].children[1] = p
        elif tree.data == "and" and tree.children[0].data == "=":
            equal = tree.children[0]
            tree.data = "="
            tree.children[0] = Node(",", "PUNCTION")
            comma = tree.children[0]
            comma.children[0] = Node(equal.children[0].data)
            tree.children[0].children[1] = Node("tau", "KEYWORD")
            tau = tree.children[0].children[1]

            tau.children[0] = Node(equal.children[0].children[1].data)
            tau = tau.children[0]
            comma = comma.children[0]
            equal = equal.children[1]

            while equal is not None:
                comma.children[1] = Node(equal.children[0].data)
                comma = comma.children[1]
                tau.children[1] = Node(equal.children[0].children[1].data)
                tau = tau.children[1]

                equal = equal.children[1]
        elif tree.data == "where":
            tree.data = "gamma"
            if tree.children[1].data == "=":
                p = tree.children[0]
                x = tree.children[1].children[0]
                e = tree.children[1].children[0].children[1]
                tree.children[0] = Node("lambda", "KEYWORD")
                tree.children[0].children[1] = e
                tree.children[0].children[0] = x
                tree.children[0].children[0].children[1] = p
        elif tree.data == "within":
            if tree.children[0].data == "=" and tree.children[0].children[1].data == "=":
                x1 = tree.children[0].children[0]
                e1 = tree.children[0].children[0].children[1]
                x2 = tree.children[0].children[1].children[0]
                e2 = tree.children[0].children[1].children[0].children[1]
                tree.data = "="
                tree.children[0] = x2
                tree.children[0].children[1] = Node("gamma", "KEYWORD")
                temp = tree.children[0].children[1]
                temp.children[0] = Node("lambda", "KEYWORD")
                temp.children[0].children[1] = e1
                temp = temp.children[0]
                temp.children[0] = x1
                temp.children[0].children[1] = e2
        elif tree.data == "rec" and tree.children[0].data == "=":
            x = tree.children[0].children[0]
            e = tree.children[0].children[0].children[1]

            tree.data = "="
            tree.children[0] = x
            tree.children[0].children[1] = Node("gamma", "KEYWORD")
            tree.children[0].children[1].children[0] = Node("YSTAR", "KEYWORD")
            ystar = tree.children[0].children[1].children[0]

            ystar.children[1] = Node("lambda", "KEYWORD")

            ystar.children[1].children[0] = Node(x)
            ystar.children[1].children[0].children[1] = Node(e)
        elif tree.data == "function_form":
            p = tree.children[0]
            v = tree.children[0].children[1]

            tree.data = "="
            tree.children[0] = p

            temp = tree
            while v.children[1].children[1] is not None:
                temp.children[0].children[1] = Node("lambda", "KEYWORD")
                temp = temp.children[0].children[1]
                temp.children[0] = Node(v)
                v = v.children[1]
            temp.children[0].children[1] = Node("lambda", "KEYWORD")
            temp = temp.children[0].children[1]

            temp.children[0] = Node(v)
            temp.children[0].children[1] = v.children[1]
        elif tree.data == "lambda":
            if tree.children[0] is not None:
                v = tree.children[0]
                temp = tree
                if v.children[1] is not None and v.children[1].children[1] is not None:
                    while v.children[1].children[1] is not None:
                        temp.children[0].children[1] = Node(
                            "lambda", "KEYWORD")
                        temp = temp.children[0].children[1]
                        temp.children[0] = Node(v)
                        v = v.children[1]

                    temp.children[0].children[1] = Node("lambda", "KEYWORD")
                    temp = temp.children[0].children[1]
                    temp.children[0] = Node(v)
                    temp.children[0].children[1] = v.children[1]
        elif tree.data == "@":
            e1 = tree.children[0]
            n = tree.children[1]
            e2 = tree.children[1].children[1]
            tree.data = "gamma"
            tree.children[0] = Node("gamma", "KEYWORD")
            tree.children[0].children[1] = e2
            tree.children[0].children[0] = n
            tree.children[0].children[0].children[1] = e1
