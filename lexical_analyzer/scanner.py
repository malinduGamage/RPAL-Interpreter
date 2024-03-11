import os
import sys
from errors_handling.error_handler import ErrorHandler
from table_routines.char_map import CharMap
from table_routines.fsa_table import FSATable
from table_routines.accept_states import AcceptStates
from utils.tokens import Token  # noqa: F401

class Scanner:
    def __init__(self):
        """
        Initialize the scanner.
        """
        self.error = ErrorHandler().handle_error
        self.charMap = CharMap().charMap
        self.fsaTable = FSATable().fsaTable
        self.acceptStates = AcceptStates().acceptStates

    # function to scan the input string and return the tokens
    def tokenScan(self, str):
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
                    f"Error1 : {chr} at line {lineNum} is not a valid character.")
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
                    f"Error2 : {token+chr} at line {lineNum} is not a valid token.")
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
                f"Error3 : {token} at line {lineNum} is not a valid token.")
            return

        return output

    # function to print the tokens
    def printer(self, lst):
        if lst != None:
            for token in lst:
                print(token)

    # function to read the input file
    def readFile(self, fileName):
        file = open(f"{fileName}", "r", encoding='utf-8')
        str = file.read()
        return str
