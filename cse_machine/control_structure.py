from utils.stack import Stack

class ControlStructure(Stack):
    def __init__(self, index):
        self.elements = []
        self.index = index

    def push(self, element):
        self.elements.append(element)
