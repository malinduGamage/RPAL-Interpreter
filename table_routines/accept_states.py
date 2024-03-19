class AcceptStates:
    def __init__(self):
        """
        Initialize the accept states for the Finite State Automaton (FSA).

        Each accept state is associated with a token type or identifier.
        """
        self.acceptStates = {
            1: 'ID',
            2: 'INT',
            3: 'OPERATOR',
            4: 'DELETE',
            5: '(',
            6: ')',
            7: ';',
            8: ',',
            9: 'STR'
        }
