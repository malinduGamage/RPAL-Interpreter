# src/table_routines/accept_states.py

#Description
# This module contains the AcceptStates class that represents the accept states for the Finite State Automaton (FSA).

#Usage
# This module provides the AcceptStates class that initializes the accept states for the FSA.

class AcceptStates:
    """
    Initialize the accept states for the Finite State Automaton (FSA).

    Each accept state is associated with a token type or identifier.
    """
    def __init__(self):
        """
        Initialize the accept states.
        """

        # Initialize the accept states dictionary with mappings of state numbers to token types
        self.acceptStates = {
            1: 'ID',          # Identifier
            2: 'INT',         # Integer
            3: 'OPERATOR',    # Operator
            4: 'DELETE',      # Delete keyword
            5: '(',           # Left parenthesis
            6: ')',           # Right parenthesis
            7: ';',           # Semicolon
            8: ',',           # Comma
            9: 'STR'          # String
        }

