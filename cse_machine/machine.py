from errors_handling.error_handler import ErrorHandler
from cse_machine.control_structure import ControlStructure
from cse_machine.enviroment import Environment
from cse_machine.stack import Stack
from cse_machine.STlinearizer import Linearizer


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
        #self._control_structure = ControlStructure()
        #self._current_environment = Environment()
        self._stack = Stack()
        self._linearizer = Linearizer()

    def execute(self, st_tree):
        """
        Execute the given Standardized Tree (ST).

        Args:
            st_tree (Node): The root node of the Standardized Tree (ST) to execute.
        """
        control_structures = self._linearizer.linearize(st_tree)
        for structure in control_structures:
            print("delta ", structure.index)
            for element in structure.elements:
                if element.type == "lambda" or element.type == "delta":
                    print(element.value+f"{element.env}",end=" ")
                else:
                    print(element.value,end=" ")
            print("\n")
