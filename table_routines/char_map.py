class CharMap:
    def __init__(self):
        """
        Initialize a character mapping dictionary.
        
        Each character is mapped to a group number based on its behavior.
        """
        self.charMap = {
            # Uppercase letters
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
            'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0,
            # Lowercase letters
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
            'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
            # Special characters and digits
            'n': 1, 't': 1, '0': 2, '1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2, '_': 3,
            '|': 4, '+': 4, '-': 4, '*': 4, '<': 4, '>': 4, '&': 4, '.': 4, '@': 4, ':': 4, '=': 4, '˜': 4, ',': 4,
            '$': 4, '!': 4, '#': 4, '%': 4, 'ˆ': 4, '[': 4, ']': 4, '{': 4, '}': 4, '"': 4, '‘': 4, '?': 4, '’': 5,
            '\\': 6, '(': 7, ')': 8, ';': 9, ',': 10, ' ': 11, '\t': 12, '\n': 13, '/': 14
        } 

    def get_category(self, char):
        """
        Get the category of a character from the character mapping dictionary.
        
        Args:
            char (str): The character to retrieve the category for.
            
        Returns:
            int: The category group number associated with the character. Returns -1 if the character
                 is not found in the mapping.
        """
        return self.charMap.get(char, -1)  # Return -1 for characters not found in the map
