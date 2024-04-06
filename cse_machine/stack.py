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
        self._environments = Stack()  # Stack to store Environment objects

    def push(self, item):
        """
        Add an item to the top of the stack.

        If the item is an instance of Environment, it is pushed to the _environments stack;
        otherwise, it is pushed to the main stack.
        """
        if isinstance(item, Environment):
            self._environments.push(item)
        super().push(item)

    def pop(self):
        """
        Remove and return the item from the top of the stack.

        If the top item is an Environment object, it is popped from the _environments stack;
        otherwise, it is popped from the main stack.
        """
        if not self._environments.is_empty():
            self._environments.pop()
        return super().pop()

    def get_nearest_environment(self):
        """
        Return the nearest Environment object from the stack without removing it.
        """
        return self._environments.peek()  # Access the top item in the _environments stack
    
    def pop_given_environment(self, env_item):
        """
        Remove and return the given Environment object from the stack.
        """
        # Remove the environment item from the main stack
        self.items.remove(env_item)
        
        # Remove the environment item from the environments stack
        self._environments.items.remove(env_item)
        
        # Return the removed environment item
        return env_item

