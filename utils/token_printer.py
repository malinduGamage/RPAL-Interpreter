from typing import List, Optional
from utils.tokens import Token  # Assuming Token class is defined in 'utils.token'

def print_tokens(tokens: Optional[List[Token]]) -> None:
    """
    Print each token in the given list of tokens.

    Args:
        tokens (Optional[List[Token]]): A list of Token objects. Can be None if no tokens are provided.
    Returns:
        None
    """
    # Check if tokens list is not None
    if tokens is not None:
        # Iterate over each token in the list
        for token in tokens:
            # Print the token
            print(token)

