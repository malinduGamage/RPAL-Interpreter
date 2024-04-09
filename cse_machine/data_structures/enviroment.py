# cse_machine/data_structures/enumeration.py

# Description
# This module defines an enumeration class for the CSE (Compiler, Symbolic, Expression) machine. 
# The enumeration class is used to represent different types of data and operations within the machine.

# Usage
# This module can be imported and used to define and handle enumerations in the CSE machine.


from collections import defaultdict

class Environment:
    index = -1

    # List of initial variables
    INITIAL_VARIABLES = [
        "Print", "Isstring", "Isinteger", "Istruthvalue",
        "Istuple", "Isfunction", "Null", "Order", "Stern",
        "Stem", "ItoS", "neg", "not", "Conc"
    ]

    def __init__(self, parent=None):
        """
        Initialize a new environment.

        Args:
            parent (Environment, optional): The parent environment. Defaults to None.
        """
        Environment.index += 1
        self.index = Environment.index
        self._environment = defaultdict(lambda: [None, None])  # name: [type, value]
        self.parent = parent

        # Initialize initial variables if this is the root environment
        if self.index == 0:
            self._initialize_initial_vars()

    def _initialize_initial_vars(self):
        """
        Initialize initial variables.
        """
        initial_vars = {var: None for var in self.INITIAL_VARIABLES}
        self._environment.update(initial_vars)

    def add_var(self, name, type, value):
        """
        Add a variable to the environment.

        Args:
            name (str): The name of the variable.
            type (str): The type of the variable.
            value (any): The value of the variable.
        """
        self._environment[name] = [type, value]

    def add_child(self, branch):
        """
        Add a child branch to the environment.

        Args:
            branch (Environment): The child branch environment.
        """
        self.children.append(branch)

    def set_parent(self, parent):
        """
        Set the parent environment.

        Args:
            parent (Environment): The parent environment.
        """
        self.parent = parent
        # Update the parent reference in the _environment dictionary
        self._environment['__parent__'] = parent._environment if parent else None
