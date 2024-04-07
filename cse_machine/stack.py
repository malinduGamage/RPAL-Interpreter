from utils.stack import Stack
from cse_machine.enviroment import Environment

class STACK(Stack):
    """
    A custom stack class that extends the Stack class and allows accessing the nearest Environment object.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        super().__init__()
        #self._environments = Stack()  # Stack to store Environment objects
        #self.stack = Stack()  # Stack to store Environment objects

    def current_environment(self):
        """
        Return the nearest Environment object from the stack without removing it.
        """
        for item in reversed(self.items):
            if item.type == "env_marker":
                return item.env
    
