class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.insert(0, child)

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
        else:
            print("Child not found")
