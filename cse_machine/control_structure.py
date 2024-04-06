from utils.stack import Stack
from cse_machine.enviroment import Environment

class ControlStructure(Stack):
    def __init__(self, environment, index):
        super().__init__()
        self.environment = environment
        self.index = index + 1
        self.bounded_variables = dict()

    

