# cse_machine/data_structures/stack.py

# Description
# This module defines a custom stack class for the CSE (Compiler, Symbolic, Expression) machine.

# Usage
# This module can be imported and used to create a custom stack class for the CSE machine.

from utils.stack import Stack
from cse_machine.data_structures.enviroment import Environment

class STACK(Stack):
    """
    A custom stack class that extends the Stack class and allows accessing the nearest Environment object.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        super().__init__()

    def current_environment(self):
        """
        Return the nearest Environment object from the stack without removing it.
        """
        for item in reversed(self.items):
            if item.type == "env_marker":
                return item.env
    
