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
        self.stack = Stack()  # Stack to store Environment objects

    def push(self, item):
        """
        Add an item to the top of the stack.

        If the item is an instance of Environment, it is pushed to the _environments stack;
        otherwise, it is pushed to the main stack.
        """
        self.stack.push(item)

    def pop(self):
        """
        Remove and return the item from the top of the stack.

        If the top item is an Environment object, it is popped from the _environments stack;
        otherwise, it is popped from the main stack.
        """
        return self.stack.pop()

    def current_environment(self):
        """
        Return the nearest Environment object from the stack without removing it.
        """
        for item in reversed(self.stack.items):
            if item.type == "env_marker":
                return item.env
    
    def size(self):
        """
        Return the number of items in the stack.
        """
        return self.stack.size()
    
    def is_empty(self):
        """
        Return whether the stack is empty.
        """
        return self.stack.is_empty()

    def peek(self):
        """
        Return the item at the top of the stack without removing it.
        """
        return self.stack.peek()
    
    def whole_stack(self):
        """
        """
        self.stack.whole_stack()
