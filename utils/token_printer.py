from typing import List, Optional
from utils.tokens import Token  # Assuming Token class is defined in 'utils.token'

def print_tokens(tokens: Optional[List[Token]]) -> None:
    """
    Print the tokens in the given list.

    Args:
        tokens (list of Token or None): List of tokens to print.
    """
    if tokens is not None:
        for token in tokens:
            print(token)

