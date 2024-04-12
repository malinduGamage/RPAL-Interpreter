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
        self.token = ""
        self.currState = 0
        self.output = []
        self.i = 0
        self.lineNum = 1


    # function to scan the input string and return the tokens
    def token_scan(self, str):
        """
        Scans the input string and returns a list of tokens.

        Parameters
        ----------
        str : str
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
        # check if the input string ends with a newline character 
        # and if so, print a warning message 
        if str[-1] != '\n':
            line = len(str.split('\n'))
            print("Potential parse problem--tokens remain.")
            print(f"Remaining tokens begin at line {line}.")

        token = ''
        currState = 0
        output = []
        i = 0
        lineNum = 1

        while i < len(str):
            chr = str[i]
            inputIndex = self.charMap.get(chr, -1)

            # track line number
            if chr == "\n":
                lineNum += 1

            # if the character is not in the charMap, throw an error
            if inputIndex == -1:
                self.error(
                    f"SCANNER : {chr} at line {lineNum} is not a valid character.")
                return

            nextState = self.fsaTable[currState][inputIndex]

            # if the next state is unacceptable and the current state is an accept state, add the token to the output and go back to the start state
            if nextState == -1 and currState in self.acceptStates:
                output.append(Token(token, self.acceptStates[currState]))
                token = ''
                currState = 0

                if chr == '\n':
                    lineNum -= 1

            # if the next state is unacceptable and the current state is not an accept state, throw an error
            elif nextState == -1 and currState not in self.acceptStates:
                self.error(
                    f"SCANNER : {token+chr} at line {lineNum} is not a valid token.")
                return
            else:
                token += chr
                i = i+1
                currState = nextState

        if currState in self.acceptStates:
            output.append(Token(token, self.acceptStates[currState]))

        # if a comment is at the end of the file without EoL, it will not be considered as an error
        elif token[0:2] == '//':
            output.append(Token(token, 'DELETE'))

        else:
            self.error(
                f"SCANNER : {token} at line {lineNum} is not a valid token.")
            return

        self.status = True
        return output
