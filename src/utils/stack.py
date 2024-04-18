# src/utils/stack.py

#Description
# This module implements the Stack data structure using a list as the underlying data structure.

#Usage
# Create a new stack using the Stack class and perform push, pop, peek, and size operations on the stack.

class Stack:
    """
    A stack is an abstract data type that serves as a collection of elements, with two main operations:
    - push, which adds an element to the top of the stack, and
    - pop, which removes the element at the top of the stack.
    The order in which elements are added to the stack is known as the stack's "order of entry" or "last-in, first-out" (LIFO).
    This implementation uses a list as the underlying data structure.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def is_empty(self):
        """
        Return whether the stack is empty.
        """
        return self.items == []

    def push(self, item):
        """
        Add an item to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the item from the top of the stack.
        """
        return self.items.pop()

    def peek(self):
        """
        Return the item at the top of the stack without removing it.
        """
        return self.items[-1]

    def size(self):
        """
        Return the number of items in the stack.
        """
        return len(self.items)
    
    def whole_stack(self):
        """
        Return the whole stack.
        """
        return self.items

