# parser/build_standard_tree.py

# Description:
# This module contains the StandardTree class, which is used to build a standard tree from a given AST tree.
# The standard tree is a transformed version of the input tree based on predefined rules and transformations outlined in the "semantics.pdf" documentation.

# Usage:
# This module provides the StandardTree class, which can be utilized to transform an input tree into a standard form.
# The build_standard_tree method applies a series of transformations to the input tree, resulting in a standard tree.
# Each transformation corresponds to specific cases or patterns found in the input tree's structure.

from utils.node import Node
from errors_handling.error_handler import ErrorHandler
from copy import deepcopy


class StandardTree:
    """
    StandardTree class is responsible for transforming an input Abstract Syntax Tree (AST) into a standard tree format.

    The standard tree is a transformed version of the input tree based on predefined rules and transformations.

    Attributes:
        binary_operators (list): List of binary operators for tree transformation.
        unary_operators (list): List of unary operators for tree transformation.
        standard_tree (Node): The transformed standard tree.
        status (bool): Flag to indicate transformation status. True if transformation is successful, otherwise False.

    Methods:
        build_standard_tree(tree): Builds the standard tree from the input tree.
        _transform_let(tree): Transforms let expression into gamma expression.
        _transform_tau(tree): Transforms tau expression into lambda expression.
        _transform_and(tree): Transforms and expression with equality into comma expression.
        _transform_function_form(tree): Transforms function_form expression into lambda expression.
        _transform_lambda(tree): Transforms lambda expression.
        _transform_within(tree): Transforms within expression.
        _transform_uop(tree): Transforms unary operator.
        _transform_conditional(tree): Transforms conditional expression.
        _transform_where(tree): Transforms where expression.
        _transform_rec(tree): Transforms rec expression.
        _transform_op(tree): Transforms binary operator.
        _transform_at(tree): Transforms at expression.
    """

    def _init_(self):
        """
        Initialize the StandardTree object.
        """
        # Error handler
        self.error_handler = ErrorHandler()

        # Operators and unary operators for tree transformation
        self.binary_operators = ["aug","or","&","+","-","/","**","gr","ge","ls","le","eq","ne","and"]
        self.unary_operators = ["not", "neg"]

        # Placeholder for the standard tree
        self.standard_tree = None

        # Flag to indicate transformation status
        self.status = True

    def build_standard_tree(self, tree):
        """
        Build the standard tree from the input tree.

        Args:
            tree (Node): The input tree to be transformed.
        """

        def traverse(tree):
            if not tree.children:
                return
            else:
                for child in tree.children:
                    traverse(child)
                self._apply_transformations(tree)

        self.standard_tree = deepcopy(tree)
        traverse(self.standard_tree)

        self.status = True

        return self.standard_tree

    def _apply_transformations(self, tree):
        """
        Apply transformations to the input tree based on specific cases.

        Args:
            tree (Node): The input tree to be transformed.
        """

        # Store the input tree for reference
        self.tree = tree

        # Apply transformations based on specific cases
        if tree.data == "let":  #
            self._transform_let(tree)
        # elif tree.data == "tau":
        #    self._transform_tau(tree)
        elif tree.data == "and":  #
            self._transform_and(tree)
        elif tree.data == "function_form":  #
            self._transform_function_form(tree)
        elif tree.data == "lambda":  #
            self._transform_lambda_1(tree)
        elif tree.data == "lambda" and (tree.children[0].data == ","):
            self._transform_lambda_2(tree)
        elif tree.data == "within":  #
            self._transform_within(tree)
        # elif tree.data in self.unary_operators:
        #     self._transform_uop(tree)
        # elif tree.data == "->":
        #     self._transform_conditional(tree)
        elif tree.data == "where":  #
            self._transform_where(tree)
        elif tree.data == "rec":  #
            self._transform_rec(tree)
        # elif tree.data in self.binary_operators:
        #     self._transform_op(tree)
        elif tree.data == "@":  #
            self._transform_at(tree)

    def _transform_let(self, tree):
        """
        Transform let expression into gamma expression.

        Args:
        -  tree (Node): The tree to be transformed.
        """
        if len(tree.children) == 2 and tree.children[0].data == "=":
            tree.data = "gamma"
            tree.children[0].data = "lambda"
            p = tree.children[1]
            tree.children[1] = tree.children[0].children[1]
            tree.children[0].children[1] = p

    def _transform_tau(self, tree):
        """
        Transform tau expression into lambda expression.

        Args:
        -  tree (Node): The tree to be transformed.
        """
        children = tree.children

        for child in children:
            tree.data = "gamma"
            tree.children = [Node("gamma"), child]
            tree.children[0].add_child(Node("<nil>"))
            tree.children[0].add_child(Node("aug"))
            tree = tree.children[0].children[1]

    def _transform_and(self, tree):
        """
        Transform and expression with equality into comma expression.

        Args:
        -  tree (Node): The tree to be transformed.
        """
        for child in tree.children:
            if child.data != "=":
                return

        tree.data = "="
        children = tree.children
        tree.children = [Node(","), Node("tau")]

        for child in reversed(children):
            tree.children[0].add_child(child.children[0])
            tree.children[1].add_child(child.children[1])

    def _transform_function_form(self, tree):
        """
        Transform function_form expression into lambda expression.

        Args:
        -  tree (Node): The tree to be transformed.
        """

        if len(tree.children) >= 3:
            tree.data = "="

            p = tree.children[0]
            v_list = tree.children[1:-1]
            e = tree.children[-1]

            tree.children = [p, Node("lambda")]

            for v in v_list:
                tree.children[1].data = "lambda"
                tree.children[1].add_child(Node("temp"))
                tree.children[1].add_child(v)
                tree = tree.children[1]
            tree.children[1] = e

    def _transform_lambda_1(self, tree):
        """
        Transform lambda expression.

        Args:
        -  tree (Node): The tree to be transformed.
        """
        if len(tree.children) >= 2:
            v_list = tree.children[:-1]
            e = tree.children[-1]
            tree.children = []
            prev = tree
            for v in v_list:
                tree.add_child(Node("lambda"))
                tree.add_child(v)
                prev = tree
                tree = tree.children[1]
            prev.children[1] = e

    def _transform_lambda_2(self, tree):
        """
        Transform lambda expression.

        Args:
        -  tree (Node): The tree to be transformed.
        """
        if len(tree.children) == 2:
            e = tree.children[1]
            v_list = tree.children[0].children
            tree.children = [Node("Temp"), Node("gamma")]
            for i in len(v_list):
                tree.children[1] = Node("gamma")
                tree.children[1].children = [Node("lambda"), Node("gamma")]
                tree.children[1].children[0].children = [v_list[i], e]
                tree.children[1].children[1].children = [
                    Node("Temp"),
                    Node(f"<INT:{i+1}>"),
                ]
                tree = tree.children[1].children[0]

    def _transform_within(self, tree):
        """
        Transform within expression.

        Args:
        - tree (Node): The tree to be transformed.
        """
        if (
            len(tree.children) == 2
            and tree.children[0].data == "="
            and tree.children[1].data == "="
        ):
            x1, e1 = tree.children[0].children
            x2, e2 = tree.children[1].children
            tree.data = "="
            tree.children = [x2, Node("gamma")]
            tree.children[1].children = [Node("lambda"), e1]
            tree.children[1].children[0].children = [x1, e2]

    def _transform_uop(self, tree):
        """
        Transform unary operator.

        Args:
            tree : The tree to transform
        """
        if len(tree.children) == 1:
            e = tree.children[0]
            tree.children = [Node(tree.data), e]
            tree.data = "gamma"

    def _transform_conditional(self, tree):
        """
        Transform conditional expression.

        Args:
            - tree (Node): The tree to be transformed.
        """
        if len(tree.children) == 3:
            b, t, e = tree.children
            tree.data = "gamma"
            tree.children = [Node("gamma"), Node("<nil>")]
            tree.children[0].children = [Node("gamma"), Node("lambda")]
            tree.children[0].children[0].children = [Node("gamma"), Node("lambda")]
            tree.children[0].children[1].children = [Node("()"), e]
            tree.children[0].children[0].children[0].children = [Node("Cond"), b]
            tree.children[0].children[0].children[1].children = [Node("()"), t]

    def _transform_where(self, tree):
        """
        Transform where expression.

        Args:
        -  tree (Node): The tree to be transformed.
        """
        if (
            len(tree.children) == 2
            and tree.children[1].data == "="
            and len(tree.children[1].children) == 2
        ):
            p = tree.children[0]
            x, e = tree.children[1].children
            tree.data = "gamma"
            tree.children = [Node("lambda"), e]
            tree.children[0].children = [x, p]

    def _transform_rec(self, tree):
        """
        Transform rec expression.

        Args:
        -  tree (Node): The tree to be transformed.
        """
        if len(tree.children) == 1 and tree.children[0].data == "=":
            x, e = tree.children[0].children
            tree.data = "="
            tree.children = [x, Node("gamma")]
            tree.children[1].children = [Node("<Y*>"), Node("lambda")]
            tree.children[1].children[1].children = [x, e]

    def _transform_op(self, tree):
        """
        Transform binary operator.

        Args:
        -  tree (Node): The tree to be transformed.
        """
        if len(tree.children) == 2:
            op_ = tree.data
            e1 = tree.children[0]
            e2 = tree.children[1]
            tree.data = "gamma"
            tree.children = [Node("gamma"), e2]
            tree.children[0].children = [Node(op_), e1]

    def _transform_at(self, tree):
        """
        Transform at expression.

        Args:
        -  tree (Node): The tree to be transformed.
        """
        if len(tree.children) == 3:
            e1 = tree.children[0]
            n = tree.children[1]
            e2 = tree.children[2]
            tree.data = "gamma"
            tree.children = [Node("gamma"), e2]
            tree.children[0].children = [n, e1]

    def get_standard_tree(self):
        """
        Get the transformed standard tree.

        Returns:
            Node: The transformed standard tree.
        """
        return self.standard_tree
