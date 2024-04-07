from utils.stack import Stack

class ControlStructure(Stack):
    def __init__(self, index):
        super().__init__()
        self.elements = self.items
        self.index = index

