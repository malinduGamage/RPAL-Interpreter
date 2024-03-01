class Scanner:
    def __init__(self):
        # symbols with same behaviour mapped to groups
        self.charMap = {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
            'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0,
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
            'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'n': 1, 't': 1,
            '0': 2, '1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2, '_': 3, '|': 4, '+': 4,
            '-': 4, '*': 4, '<': 4, '>': 4, '&': 4, '.': 4, '@': 4, ':': 4, '=': 4, '˜': 4, ',': 4, '$': 4, '!': 4,
            '#': 4, '%': 4, 'ˆ': 4, '[': 4, ']': 4, '{': 4, '}': 4, '"': 4, '‘': 4, '?': 4, '’': 5, '\\': 6, '(': 7,
            ')': 8, ';': 9, ',': 10, ' ': 11, '\t': 12, '\n': 13, '/': 14
        }
        
        # table for the finite state automata
        self.fsaTable = [
            [1, 1, 2, -1, 3, 11, -1, 5, 6, 7, 8, 4, 4, 4, 3],
            [1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,],
            [-1, -1, -1, -1, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, 4, 4, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 4, 10],
            [-1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [12, 12, 12, 12, 12, 14, 13, 12, 12, 12, 12, 12, -1, -1, 12],
            [-1, 12, -1, -1, -1, 15, 12, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        ]
        
        self.acceptStates = {
            1: 'IDENTIFIER',
            2: 'INTEGER',
            3: 'OPERATOR',
            4: 'DELETE',
            5: '(',
            6: ')',
            7: ';',
            8: ',',
            9: 'STRING'
        }

    # function to scan the input string and return the tokens
    def tokenScan(self, str):
        token = ''
        currState = 0
        output = []
        i = 0

        while i < len(str):
            chr = str[i]
            inputIndex = self.charMap.get(chr, -1)

            if inputIndex == -1:
                print("error")
                return

            nextState = self.fsaTable[currState][inputIndex]

            # if the next state is unacceptable and the current state is an accept state, add the token to the output and go back to the start state
            if nextState == -1 and currState in self.acceptStates:
                output.append((token, self.acceptStates[currState]))
                token = ''
                currState = 0
            # if the next state is unacceptable and the current state is not an accept state, throw an error
            elif nextState == -1 and currState not in self.acceptStates:
                print(f"error - {token+chr}")
                return
            else:
                token += chr
                i = i+1
                currState = nextState

        if currState in self.acceptStates:
            output.append((token, self.acceptStates[currState]))
        else:
            # if a comment is at the end of the file, it will be added to the output
            if token[0:2] == '//':
                output.append((token, 'DELETE'))
            else:
                print(f"error - {token}")
                return

        return output

    # function to screen out DELETE tokens
    def tokenScreen(self, tokenArray):
        screenedTokenArray = []
        for token in tokenArray:
            if token[1] != 'DELETE':
                screenedTokenArray.append(token)
        return screenedTokenArray

    # function to print the tokens
    def printer(self, lst):
        if lst != None:
            for i in lst:
                print(i)

    # function to read the input file
    def readFile(self, fileName):
        file = open(f"{fileName}", "r", encoding='utf-8')
        str = file.read()
        return str