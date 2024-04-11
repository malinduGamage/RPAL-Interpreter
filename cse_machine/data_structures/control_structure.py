#cse_machine/data_structures/control_structure.py

# Description
# This module defines a control structure class for the CSE (Compiler, Symbolic, Expression) machine.

# Usage
# This module contains the ControlStructure class, which represents a control structure in the CSE machine.


from utils.stack import Stack

class ControlStructure(Stack):
    """
    Represents a control structure in the CSE (Compiler, Symbolic, Expression) machine.
    Inherits from Stack class.

    Attributes:
        elements (list): List of elements in the control structure.
        index (int): Index of the control structure.
    """

    def __init__(self, index):
        """
        Initializes a new control structure.

        Args:
            index (int): Index of the control structure.
        """
        # Initialize the control structure
        super().__init__()
        self.elements = self.items  # Alias for the items attribute inherited from Stack
        self.index = index
