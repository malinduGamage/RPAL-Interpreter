
from utils.node import Node


class standard_tree:
    def __init__(self):
        self.standard_tree = None
        self.status = False

    def build_standard_tree(self, tree):

        if tree.data == "let":
            tree.data = "gamma"
            tree.children[0].data = "lambda"
            p = tree.children[1]
            tree.children[1] = tree.children[0].children[1]
            tree.children[0].children[1] = p
