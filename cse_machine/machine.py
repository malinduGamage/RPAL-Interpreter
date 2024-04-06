from errors_handling.error_handler import ErrorHandler
from cse_machine.control_structure import ControlStructure
from cse_machine.environment import Environment
from cse_machine.STlinearizer import Linearizer
from cse_machine.stack import Stack

class CSEMachine:
    """
    Class representing the Control Structure Environment (CSE) machine for executing RPAL programs.

    Attributes:
        _error_handler (ErrorHandler): Error handler instance for managing errors during execution.
        _linearizer (Linearizer): Linearizer instance for converting the Standardized Tree (ST) to linear form.
        _control_structure (ControlStructure): ControlStructure instance for managing control flow.
        _current_environment (Environment): Environment instance representing the current execution environment.
        _stack (Stack): Stack instance for managing the execution stack.
    """

    def __init__(self):
        """
        Initialize the CSEMachine with necessary components.
        """
        self._error_handler = ErrorHandler()
        self._linearizer = Linearizer()
        self._control_structure = ControlStructure(self._linearizer)
        self._current_environment = Environment()
        self._stack = Stack()

    # Add more methods for executing RPAL programs, managing control flow, etc.



    