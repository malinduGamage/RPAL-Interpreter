#src/cse_machine/binary_operations/apply_bin.py

# Description
# This module defines functions to apply binary operations to operands in the CSE (Compiler, Symbolic, Expression) machine.

# Usage
# This module can be imported and used to apply binary operations to operands in the CSE machine.

# This file contains functions to apply unary and binary operations to operands in the CSE machine.
from src.utils.control_structure_element import ControlStructureElement

def apply_binary(cse_machine, rator, rand, binop):
    """
    This function applies a binary operation to two operands, based on the specified binary operator.

    Parameters
    ----------
    cse_machine: CSEMachine
        The CSE machine used to evaluate the expression.
    rator: object
        The left operand of the binary operation.
    rand: object
        The right operand of the binary operation.
    binop: str
        The binary operator to apply.

    Returns
    -------
    object
        The result of the binary operation.

    Raises
    ------
    ValueError
        If the binary operator is not recognized.
    """

    # Dictionary mapping binary operators to their corresponding functions
    binary_operators = {
            "aug" : lambda cse_machine, rator, rand : apply_aug(cse_machine, rator, rand),
            "or"  : lambda cse_machine, rator, rand : apply_or(cse_machine, rator, rand),
            "&"   : lambda cse_machine, rator, rand : apply_and(cse_machine, rator, rand),
            "+"   : lambda cse_machine, rator, rand : apply_arithmetic(cse_machine, rator, rand, lambda a, b: a + b),
            "-"   : lambda cse_machine, rator, rand : apply_arithmetic(cse_machine, rator, rand, lambda a, b: a - b),
            "*"   : lambda cse_machine, rator, rand : apply_arithmetic(cse_machine, rator, rand, lambda a, b: a * b),
            "/"   : lambda cse_machine, rator, rand : apply_arithmetic(cse_machine, rator, rand, lambda a, b: a // b),
            "**"  : lambda cse_machine, rator, rand : apply_arithmetic(cse_machine, rator, rand, lambda a, b: a ** b),
            "gr"  : lambda cse_machine, rator, rand : apply_comparison(cse_machine, rator, rand, lambda a, b: a > b),
            "ge"  : lambda cse_machine, rator, rand : apply_comparison(cse_machine, rator, rand, lambda a, b: a >= b),
            "ls"  : lambda cse_machine, rator, rand : apply_comparison(cse_machine, rator, rand, lambda a, b: a < b),
            "le"  : lambda cse_machine, rator, rand : apply_comparison(cse_machine, rator, rand, lambda a, b: a <= b),
            "eq"  : lambda cse_machine, rator, rand : apply_eq(cse_machine, rator, rand),
            "ne"  : lambda cse_machine, rator, rand : apply_ne(cse_machine, rator, rand),
            "Conc": lambda cse_machine, rator, rand : apply_conc(cse_machine, rator, rand)
                    }

    # Get the operation function corresponding to the binary operator
    operation_function = binary_operators.get(binop)
    if operation_function:
        # Apply the operation function with the provided operands
        return operation_function(cse_machine, rator, rand)
    else:
        # If the binary operator is not recognized, raise an error
        raise ValueError("Invalid binary operation: " + binop)

# Function to handle the 'aug' binary operator
def apply_aug(cse_machine, rator, rand):
    """
    This function applies a binary operation to two operands, based on the specified binary operator.

    Parameters
    ----------
    cse_machine : CSEMachine
        The CSE machine used to evaluate the expression.
    rator : object
        The left operand of the binary operation.
    rand : object
        The right operand of the binary operation.

    Returns
    -------
    object
        The result of the binary operation.

    Raises
    ------
    ValueError
        If the binary operator is not recognized.
    """
    
    if rator.type == "nil" :
        return ControlStructureElement("tuple", [rand])
    elif rand.type == "nil":
        if rator.type == "tuple":
            # If the right operand is "nil", return the left operand
            rator.value.append(rand)
            return rator
        return rator
    elif rator.type in ["tuple","ID","INT","STR","bool"] and rand.type in ["tuple","ID","INT","STR","bool"]:
        if isinstance(rator.value, list) :
            ls = rator.value.copy()
            ls.append(rand)
            res = ControlStructureElement("tuple", ls)
            return res
        return ControlStructureElement("tuple", [rator, rand])
    else:
        return cse_machine._error_handling.handle_error("Cannot augment a non tuple (2).")

# Function to handle the 'or' binary operator
def apply_or(cse_machine, rator, rand):
    """
    This function applies a binary operation to two operands, based on the specified binary operator.

    Parameters
    ----------
    cse_machine : CSEMachine
        The CSE machine used to evaluate the expression.
    rator : object
        The left operand of the binary operation.
    rand : object
        The right operand of the binary operation.

    Returns
    -------
    object
        The result of the binary operation.

    Raises
    ------
    ValueError
        If the binary operator is not recognized.
    """
    if isinstance(rator, bool) and isinstance(rand, bool):
        # If both operands are boolean, return the logical OR of them
        return rator or rand
    else:
        # Otherwise, raise an error
        raise cse_machine._error_handling.handle_error("Invalid value used in logical expression 'or'")

# Function to handle the 'and' binary operator
def apply_and(cse_machine, rator, rand):
    """
    This function applies a binary operation to two operands, based on the specified binary operator.

    Parameters
    ----------
    cse_machine : CSEMachine
        The CSE machine used to evaluate the expression.
    rator : object
        The left operand of the binary operation.
    rand : object
        The right operand of the binary operation.

    Returns
    -------
    object
        The result of the binary operation.

    Raises
    ------
    ValueError
        If the binary operator is not recognized.
    """
    if isinstance(rator, bool) and isinstance(rand, bool):
        # If both operands are boolean, return the logical AND of them
        return rator and rand
    else:
        # Otherwise, raise an error
        raise ValueError("Illegal Operands for '&'")

# Function to handle the 'eq' binary operator
def apply_eq(cse_machine, rator, rand):
    """
    This function applies a binary operation to two operands, based on the specified binary operator.

    Parameters
    ----------
    cse_machine : CSEMachine
        The CSE machine used to evaluate the expression.
    rator : object
        The left operand of the binary operation.
    rand : object
        The right operand of the binary operation.

    Returns
    -------
    bool
        The result of the binary operation.

    Raises
    ------
    ValueError
        If the binary operator is not recognized.
    """
    if type(rator) == type(rand):
        # If the types of both operands are the same, return whether they are equal
        return rator == rand
    else:
        # Otherwise, raise an error
        raise cse_machine._error_handling.handle_error("Illegal Operands for 'eq'")

# Function to handle the 'ne' binary operator
def apply_ne(cse_machine, rator, rand):
    """
    This function applies a binary operation to two operands, based on the specified binary operator.

    Parameters
    ----------
    cse_machine : CSEMachine
        The CSE machine used to evaluate the expression.
    rator : object
        The left operand of the binary operation.
    rand : object
        The right operand of the binary operation.

    Returns
    -------
    bool
        The result of the binary operation.

    Raises
    ------
    ValueError
        If the binary operator is not recognized.
    """
    if type(rator) == type(rand):
        # If the types of both operands are the same, return whether they are not equal
        return rator != rand
    else:
        # Otherwise, raise an error
        raise cse_machine._error_handling.handle_error("Illegal Operands for 'ne'")

# Function to handle arithmetic operations
def apply_arithmetic(cse_machine, rator, rand, operation):
    """
    This function applies an arithmetic operation to two operands, based on the specified operation function.

    Parameters
    ----------
    cse_machine : CSEMachine
        The CSE machine used to evaluate the expression.
    rator : object
        The left operand of the arithmetic operation.
    rand : object
        The right operand of the arithmetic operation.
    operation : Callable[[int, int], int]
        The arithmetic operation to apply.

    Returns
    -------
    int
        The result of the arithmetic operation.

    Raises
    ------
    ValueError
        If the operands are not integers or the operation is not a function.
    """
    if isinstance(rator, int) and isinstance(rand, int):
        # If both operands are integers, apply the specified arithmetic operation
        return operation(rator, rand)
    else:
        # Otherwise, raise an error
        raise cse_machine._error_handler.handle_error("Illegal Operands for Arithmetic Operation")

def apply_conc(cse_machine,rator,rand):
    """
    This function applies a binary operation to two operands, based on the specified binary operator.
    
    Parameters
    ----------
    cse_machine : CSEMachine
    rator : object
    rand : object
    
    Returns
    -------
    str
    Raises
    ------
    ValueError
    """
    
    if isinstance(rator, str) and isinstance(rand, str):
        return rator + rand
    else:
        raise cse_machine._error_handler.handle_error("Non-strings used in conc call")
    
# Function to handle comparison operations
def apply_comparison(cse_machine, rator, rand, operation):
    """
    This function applies a comparison operation to two operands, based on the specified operation function.

    Parameters
    ----------
    cse_machine : CSEMachine
        The CSE machine used to evaluate the expression.
    rator : object
        The left operand of the comparison operation.
    rand : object
        The right operand of the comparison operation.
    operation : Callable[[int, int], int]
        The comparison operation to apply.

    Returns
    -------
    bool
        The result of the comparison operation.

    Raises
    ------
    ValueError
        If the operands are not integers or the operation is not a function.
    """
    if (isinstance(rator, int) and isinstance(rand, int)) or (isinstance(rator, str) and isinstance(rand, str)):
        # If both operands are integers, apply the specified comparison operation
        return operation(rator, rand)
    else:
        # Otherwise, raise an error
        raise cse_machine._error_handler.handle_error("Illegal Operands for 'gr'")
