#cse_machine/binary_operations/apply_bin.py

# Description
# This module defines functions to apply binary operations to operands in the CSE (Compiler, Symbolic, Expression) machine.

# Usage
# This module can be imported and used to apply binary operations to operands in the CSE machine.

from utils.control_structure_element import ControlStructureElement
def apply_unary(cse_machine, rator_e, unop):
    """
    Apply a unary operation to an operand.

    Args:
        cse_machine (CSEMachine): The CSE machine instance.
        rator_e (RatorExpr): The operand expression.
        unop (str): The unary operation to apply.

    Returns:
        Expr: The result of the operation.

    Raises:
        ValueError: If the unary operation is not recognized.
    """
    rator = rator_e.value
    # Dictionary mapping binary operators to their corresponding functions
    unary_operators = {
            "Print": lambda cse_machine, operand: apply_print(cse_machine, operand),
            "Isstring": lambda cse_machine, operand: operand.type == "STR",
            "Isinteger": lambda cse_machine, operand: operand.type == "INT" ,
            "Istruthvalue": lambda cse_machine, operand: operand.type == "bool",
            "Isfunction": lambda cse_machine, operand: operand.type == "lambda",
            "Null": lambda cse_machine, operand: operand.type == "nil",
            "Istuple": lambda cse_machine, operand: isinstance(operand.value, list) or operand.type == "nil",
            "Order": lambda cse_machine, operand: apply_order(cse_machine, operand),
            "Stern": lambda cse_machine, operand: apply_stern(cse_machine, operand.value),
            "Stem": lambda cse_machine, operand: apply_stem(cse_machine, operand.value),
            "ItoS": lambda cse_machine, operand: str(operand.value) if isinstance(operand.value, int) and not isinstance(operand.value, bool) else cse_machine._error_handler.handle_error("CSE : Invalid unary operation"),
            "neg": lambda cse_machine, operand: -operand.value if isinstance(operand.value, int) else cse_machine._error_handler.handle_error("CSE : Invalid unary operation"),
            "not": lambda cse_machine, operand: not operand.value if isinstance(operand.value, bool) else cse_machine._error_handler.handle_error("CSE : Invalid unary operation"),
        }
    # Get the operation function corresponding to the binary operator
    operation_function = unary_operators.get(unop)
    if operation_function:
        # Apply the operation function with the provided operands
        return operation_function(cse_machine, rator_e)
    else:
        # If the binary operator is not recognized, raise an error
        raise ValueError("Invalid binary operation: " + unop)

# Function to apply the Print unary operator
def apply_print(cse_machine, operand):
    """
    Apply the Print unary operation to an operand.

    Args:
        cse_machine (CSEMachine): The CSE machine instance.
        operand (Expr): The operand expression.

    Returns:
        Expr: A dummy value.

    """
    element = operand.value
    # Define the covertToString function
    def covert_to_string(element):
        if isinstance(element, list):
            out = ""
            return convert_list(element,out)
        elif element == "lambda":
            x = "".join(x for x in operand.bounded_variable)
            k = str(operand.control_structure)
            return "[lambda closure: " + x + ": " + k + "]"
        elif isinstance(element, bool):
            return "true" if element else "false"
        elif isinstance(element, str):
            return element
        elif isinstance(element, int):
            return str(element)
        elif element == None:
            return "nil"
        else:
            raise TypeError("Unknown element type.")
        
    def convert_list(element,out):
        if isinstance(element, list):
            out += "("
            for el in element:
                out = convert_list(el,out)
            out = out[:-2] +  ")"
        else:
            if isinstance(element.value, list):
                out += "("
                for el in element.value:
                    out = convert_list(el,out)
                out = out[:-2] +  "), "
            else:
                out += str(element.value) + ", "
        return out
    # convert the element to a string
    cse_machine._outputs.append(covert_to_string(element).replace("\\n", "\n").replace("\\t", "\t"))
    
    # Return a dummy value
    return "dummy"


# Function to apply the Order unary operator
def apply_order(cse_machine, operand):
    """
    Apply the Order unary operation to an operand.

    Args:
        cse_machine (CSEMachine): The CSE machine instance.
        operand (Expr): The operand expression.

    Returns:
        int: The ASCII value of the first character of the operand.

    Raises:
        ValueError: If the operand is not a string.
    """
    if isinstance(operand.value, list):
        return len(operand.value)
    elif operand.type == "nil":
        return 0
    else:
        cse_machine._error_handler.handle_error("CSE : Invalid unary operation")

# Function to apply the Stern unary operator
def apply_stern(cse_machine, operand):
    """
    Apply the Stern unary operation to an operand.

    Args:
        cse_machine (CSEMachine): The CSE machine instance.
        operand (Expr): The operand expression.

    Returns:
        str: The first character of the operand.

    Raises:
        ValueError: If the operand is not a string or is empty.
    """
    if isinstance(operand, str) and len(operand) >= 1:
        return operand[1:]
    else:
        cse_machine._error_handler.handle_error("CSE : Invalid unary operation")

def apply_stem(cse_machine, operand):
    """
    Apply the Stem unary operation to an operand.

    Args:
        cse_machine (CSEMachine): The CSE machine instance.
        operand (Expr): The operand expression.

    Returns:
        str: The remaining characters of the operand.

    Raises:
        ValueError: If the operand is not a string or is empty.
    """
    if isinstance(operand, str) and len(operand) >= 1:
        return operand[0]
    else:
        cse_machine._error_handler.handle_error("CSE : Invalid unary operation")