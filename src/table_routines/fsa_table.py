# src/table_routines/fsa_table.py

# Description
# This module contains the FSATable class that represents the transition table for the Finite State Automaton (FSA).

# Usage
# This function provides the FSATable class that initializes the transition table for the FSA.
class FSATable:
    """
    Initialize the Finite State Automaton (FSA) transition table.

    The table represents transitions between states based on input symbols.
    Each row corresponds to a state, and each column corresponds to an input symbol.
    The value at row i and column j represents the next state to transition to when
    in state i and encountering input symbol j. If the value is -1, it indicates
    that there is no transition defined for that state and input symbol combination.
    """

    def __init__(self):
        """
        Initialize the FSA table.
        """
        self.fsaTable = [
            [ 1,  1,  2, -1,  3, 11, -1,  5,  6,  7,  8,  4,  4,  4,  3],
            [ 1,  1,  1,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1,  2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1,  3, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  4,  4,  4, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  4, 10],
            [11, 11, 11, 11, 11,  9, 12, 11, 11, 11, 11, 11, -1, -1, 11],
            [-1, 11, -1, -1, -1, 11, 11, -1, -1, -1, -1, -1, -1, -1, -1],
        ]
