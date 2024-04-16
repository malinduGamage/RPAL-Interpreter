# lexical_analyzer/scanner.py

# Description:
# This file contains the Scanner class, which is responsible for scanning the input string and returning a list of tokens. 
# It utilizes a character map, a Finite State Automaton (FSA) table, and a set of accept states to perform lexical analysis.

# Usage:
# The Scanner class provides the token_scan() method, which scans the input string and returns a list of tokens.
# To use the Scanner, create an instance of the Scanner class and call the token_scan() method with the input string.
# The token_scan() method takes a single argument, the input string to be scanned, and returns a list of Token objects.
# If the input string contains any invalid characters or tokens, the Scanner class raises a ScannerError.

import os
import sys
from errors_handling.error_handler import ErrorHandler
from table_routines.char_map import CharMap
from table_routines.fsa_table import FSATable
from table_routines.accept_states import AcceptStates
from utils.tokens import Token


class Scanner:
    """
    Initialize and manage the scanner for the RPAL interpreter.

    The Scanner class is responsible for scanning the input string and identifying tokens based on a predefined set of characters and states. It utilizes a character map, Finite State Automaton (FSA) table, and accept states to perform lexical analysis.

    Attributes:
        error (method): A method to handle errors encountered during scanning.
        charMap (dict): A dictionary mapping characters to their corresponding indices for lookup.
        fsaTable (list of lists): A 2D list representing the Finite State Automaton table for transition states.
        acceptStates (set): A set containing accept states in the Finite State Automaton.
        status (bool): A flag indicating the current status of the scanner.

    Methods:
        token_scan(str): Scans the input string and returns a list of tokens.

    """
    def __init__(self):
        """
        Initialize the scanner.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        # Initialize the scanner with character map, FSA table, and accept states
        self.error = ErrorHandler().handle_error
        self.charMap = CharMap().charMap
        self.fsaTable = FSATable().fsaTable
        self.acceptStates = AcceptStates().acceptStates
        self.status = False

        # Initialize the scanner state variables and output list variables
        self.current_token = str()
        self.current_state = 0
        self.output_tokens = list()
        self.index = 0
        self.line_number = 1


    def token_scan(self, input_string):
        """
        Scans the input string and returns a list of tokens.

        Parameters
        ----------
        input_string : str
            The input string to be scanned.

        Returns
        -------
        List[Token]
            A list of tokens generated from the input string.

        Raises
        ------
        ScannerError
            If an invalid character or token is encountered.
        """
        self.input_string = input_string
        
        # Check if the input string ends with a newline character
        # and if not, print a warning message
        check_ending_newline(input_string)

        while self.index < len(input_string):
            character = input_string[self.index]
            input_index = self.charMap.get(character, -1)

            # Track line number
            if character == "\n":
                self.line_number += 1

            # If the character is not in the charMap, throw an error
            if input_index == -1:
                self.error(
                    f"SCANNER : {character} at line {self.line_number} is not a valid character.")
                return

            next_state = self.fsaTable[self.current_state][input_index]

            # If the next state is unacceptable and the current state is an accept state,
            # add the token to the output and go back to the start state
            if next_state == -1 and self.current_state in self.acceptStates:
                self.output_tokens.append(Token(self.current_token, self.acceptStates[self.current_state]))
                self.current_token = ''
                self.current_state = 0

                if character == '\n':
                    self.line_number -= 1

            # If the next state is unacceptable and the current state is not an accept state, throw an error
            elif next_state == -1 and self.current_state not in self.acceptStates:
                self.error(
                    f"SCANNER : {self.current_token + character} at line {self.line_number} is not a valid token.")
                return
            else:
                self.current_token += character
                self.index += 1
                self.current_state = next_state

        if self.current_state in self.acceptStates:
            self.output_tokens.append(Token(self.current_token, self.acceptStates[self.current_state]))

        # If a comment is at the end of the file without EoL, it will not be considered as an error
        elif self.current_token[0:2] == '//':
            self.output_tokens.append(Token(self.current_token, 'DELETE'))

        else:
            self.error(
                f"SCANNER : {self.current_token} at line {self.line_number} is not a valid token.")
            return

        self.status = True
        return self.output_tokens


##################################################################################################
# Helper functions (parser errors detection)
##################################################################################################

def check_ending_newline(input_string):
    """
    Checks if the input string ends with a new line character. If not, it raises a potential parsing error.

    Parameters:
        self (Scanner object): The Scanner object.

    Returns:
        None

    Raises:
        ScannerError: If the input string does not end with a new line character.
    """
    if input_string[-1] != '\n':
        line = len(input_string.split('\n'))
        print("Potential parse problem -- tokens remain.")
        print(f"Remaining tokens begin at line {line}.")

