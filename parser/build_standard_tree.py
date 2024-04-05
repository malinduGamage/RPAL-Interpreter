# parser/build_standard_tree.py

# Description:
# This module contains the StandardTree class, which is used to build a standard tree from a given ast tree. 
# The standard tree is a transformed version of the input tree based on predefined rules and transformations.

# Usage:
# This module provides the StandardTree class, which can be utilized to transform an input tree into a standard form.
# The build_standard_tree method applies a series of transformations to the input tree, resulting in a standard tree.
# Each transformation corresponds to specific cases or patterns found in the input tree's structure.

from utils.node import Node
class StandardTree:
    def __init__(self):
        """
        Initialize the StandardTree object.

        Args:
        - tree: The input tree to be transformed.
        """
        # Operators and unary operators for tree transformation
        self.binary_operators = ["aug", "or", "&", "+", "-", "/", "**", "gr","ge","ls","le","eq","ne","and"]
        self.unary_operators = ["not", "neg"]

        # Original input tree
        self.tree = None
        
        # Placeholder for the standard tree
        self.standard_tree = None
        
        # Flag to indicate transformation status
        self.status = False

    def build_standard_tree(self,tree):
        """
        Build the standard tree from the input tree.
        """
        self.tree = tree
        
        # Apply transformations based on specific cases
        if tree.data == "let":
            self._transform_let(tree) 
######################################################################## Done #######################################################
        elif tree.data == "tau":
            self._transform_tau(tree)
        elif tree.data == "and" and tree.children[0].data == "=":
            self._transform_and(tree)   
        elif tree.data == "function_form":
            self._transform_function_form(tree)   
        elif tree.data == "lambda" and (tree.children[0] is not None):
            self._transform_lambda(tree)
######################################################################## Done #######################################################
        elif tree.data == "within" and tree.children[0].data == "=" and tree.children[1].data == "=":
            self._transform_within(tree)       
        elif tree.data in self.unary_operators :
            self._transform_uop(tree)
        elif tree.data == "->" :
            self._transform_conditional(tree)
        elif tree.data == "where" and tree.children[1].data == "=":
            self._transform_where(tree.children)
        elif tree.data == "rec" and tree.children[0].data == "=":
            self._transform_rec(tree.children)
        elif tree.data in self.binary_operators:
            self._transform_op(tree)
        elif tree.data == "@":
            self._transform_at(tree)
    
    def _transform_let(self, tree):
        """
        Transform let expression into gamma expression.

        Args:
        - tree: The tree to be transformed.
        """
        tree.data = "gamma"
        tree.children[0].data = "lambda"
        p = tree.children[1]
        tree.children[1] = tree.children[0].children[1]
        tree.children[0].children[1] = p
######################################################################## Done #######################################################
    def _transform_tau(self, tree):
        """
        Transform tau expression into lambda expression.

        Args:
        - tree: The tree to be transformed.
        """
        tree.data = "lambda"
        tree.children[0].data = "tau"
        tau = tree.children[0].children[1]

    def _transform_and(self, tree):
        """
        Transform and expression with equality into comma expression.

        Args:
        - tree: The tree to be transformed.
        """
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

    def _transform_function_form(self, tree):
        """
        Transform function_form expression into lambda expression.

        Args:
        - tree: The tree to be transformed.
        """
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
        
    def _transform_lambda(self, tree):
        """
        Transform lambda expression.

        Args:
        - tree: The tree to be transformed.
        """
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
    def _transform_within(self,tree):
        """
        Transform within expression.

        Args:
        - tree: The tree to be transformed.
        """
        print("@",tree)
        print("#",tree.children[0].children)
        print("&",tree.children[1].children)
        x1 , e1 = tree.children[0].children
        x2 , e2 = tree.children[1].children
        tree.data = "="
        tree.children = [x2,Node("gamma")]
        tree.children[1].children = [Node("lambda"),e1]
        tree.children[1].children[0].children = [x1,e2]
    
    def _transform_uop(self, tree):
        """
        Transform unary operator.

        Args:
            tree : The tree to transform
        """
        e = tree.children[0]
        tree.children = [Node(tree.data),e]
        tree.data = "gamma"

    def _transform_conditional(self, tree):
        """
        Transform conditional expression.

        Args:
            tree : The tree to transform
        """
        b , t, e = tree.children
        tree.data = "gamma"
        tree.children = [Node("gamma"),Node("nil")]
        tree.children[0].children = [Node("gamma"),Node("lambda")]
        tree.children[0].children[0].children = [Node("gamma"),Node("lambda")]
        tree.children[0].children[1].children = [Node("()"),Node("e")]
        tree.children[0].children[0].children[0].children = [Node("Cond"),Node("B")]
        tree.children[0].children[0].children[1].children = [Node("()"),Node("T")]
    def _transform_where(self, tree):
        """
        Transform where expression.

        Args:
        - tree: The tree to be transformed.
        """
        e1 = tree.children[0]
        e2 = tree.children[1]
        tree.data = "gamma"
        tree.children = [Node("gamma"),e2]
        p = tree.children[0]
        x ,e = tree.children[1].children
        tree.data = "gamma"
        tree.children = [Node("lambda"),e]
        tree.children[0].children = [x,p]
        
    def _transform_rec(self, tree):
        """
        Transform rec expression.

        Args:
        - tree: The tree to be transformed.
        """
        x , e = tree.children[0].children
        tree.data = "="
        tree.children = [x, Node("gamma")]
        tree.children[1].children = [Node("Ystar"),Node("lambda")]
        tree.children[1].children[1].children = [x,e]

    def _transform_op(self, tree):
        """
        Transform binary operator.

        Args:
        - tree: The tree to be transformed.
        """
        op_ = tree.data
        e1 = tree.children[0]
        e2 = tree.children[1]
        tree.data = "gamma"
        op_ = tree.data
        e1 = tree.children[0]
        e2 = tree.children[1]
        tree.data = "gamma"
        tree.children = [Node("gamma"),e2]
        tree.children[0].children = [Node(op_),e1]

    def _transform_at(self,tree):
        """
        Transform at expression.

        Args:
        - tree: The tree to be transformed.
        """
        e1 = tree.children[0]
        n = tree.children[1]
        e2 = tree.children[2]
        tree.data = "gamma"
        tree.children = [Node("gamma"),e2]
        tree.children[0].children = [n,e1]