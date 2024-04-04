
from utils.node import Node


class standard_tree:
    def __init__(self, tree):
        self.op = ["aug","or","&","+","-","/","**","gr"]
        self.uop = ["not","neg"]
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
######################################################################## Done #######################################################
        elif tree.data == "and" and tree.children[0].data == "=":
            equal = tree.children[0]
            tree.data = "="
            tree.children[0] = Node(",")
            comma = tree.children[0]
            comma.children[0] = Node(equal.children[0].data)
            tree.children[0].children[1] = Node("tau")
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

######################################################################## Done #######################################################
        elif tree.data == "within" and tree.children[0].data == "=" and tree.children[1].data == "=":
            x1 , e1 = tree.children[0].children
            x2 , e2 = tree.children[1].children
            tree.data = "="
            tree.children = [x2,Node("gamma")]
            tree.children[1].children = [Node("lambda"),e1]
            tree.children[1].children[0].children = [x1,e2]
        elif tree.data in self.uop :
            e = tree.children[0]
            tree.children = [Node(tree.data),e]
            tree.data = "gamma"
        elif tree.data == "->" :
            b , t, e = tree.children
            tree.data = "gamma"
            tree.children = [Node("gamma"),Node("nil")]
            tree.children[0].children = [Node("gamma"),Node("lambda")]
            tree.children[0].children[0].children = [Node("gamma"),Node("lambda")]
            tree.children[0].children[1].children = [Node("()"),Node("e")]
            tree.children[0].children[0].children[0].children = [Node("Cond"),Node("B")]
            tree.children[0].children[0].children[1].children = [Node("()"),Node("T")]

        
        elif tree.data == "neg" :
            e = tree.children[0]
            tree.data = "gamma"
            tree.children = [Node("neg"),e]
        
        elif tree.data == "where" and tree.children[1].data == "=":
            p = tree.children[0]
            x ,e = tree.children[1].children
            tree.data = "gamma"
            tree.children = [Node("lambda"),e]
            tree.children[0].children = [x,p]


        elif tree.data == "rec" and tree.children[0].data == "=":
            x , e = tree.children[0].children

            tree.data = "="
            tree.children = [x, Node("gamma")]
            tree.children[1].children = [Node("Ystar"),Node("lambda")]
            tree.children[1].children[1].children = [x,e]
        
        elif tree.data in self.op:
            op_ = tree.data
            e1 = tree.children[0]
            e2 = tree.children[1]
            tree.data = "gamma"
            tree.children = [Node("gamma"),e2]
            tree.children[0].children = [Node(op_),e1]
        elif tree.data == "@":
            e1 = tree.children[0]
            n = tree.children[1]
            e2 = tree.children[2]
            tree.data = "gamma"
            tree.children = [Node("gamma"),e2]
            tree.children[0].children = [n,e1]
