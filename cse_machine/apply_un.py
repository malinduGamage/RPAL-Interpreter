def apply_unary(cse_machine, rator_e, unop):
    rator = rator_e.value
    # Dictionary mapping binary operators to their corresponding functions
    unary_operators = {
            "Print": lambda cse_machine, operand: apply_print(cse_machine, operand),
            "Isstring": lambda cse_machine, operand: isinstance(operand.value, str),
            "Isinteger": lambda cse_machine, operand: isinstance(operand.value, int),
            "Istruthvalue": lambda cse_machine, operand: isinstance(operand.value, bool),
            "Isfunction": lambda cse_machine, operand: "lambda"==operand.type,
            "Null": lambda cse_machine, operand: operand.type == "nil",
            "Istuple": lambda cse_machine, operand: isinstance(operand.value, list),
            "Order": lambda cse_machine, operand: len(operand.value) if isinstance(operand.value, list) else cse_machine._error_handler.handle_error("CSE : Invalid unary operation"),
            "Stern": lambda cse_machine, operand: apply_stern(cse_machine, operand.value),
            "Stem": lambda cse_machine, operand: apply_stem(cse_machine, operand.value),
            "ItoS": lambda cse_machine, operand: str(operand.value),
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
    element = operand.value
    # Define the covertToString function
    def covert_to_string(element):
        if isinstance(element, list):
            out = "( "
            for el in element:
                out += str(el.value) + " , "
            return out[:-2]+")"
        elif isinstance(element, str) or isinstance(element, int):
            return str(element)
        elif element == "lambda":
            x = operand.bounded_variable
            k = operand.control_structure

            return "[lambda closure: " + x + ": " + k + "]"
        else:
            raise TypeError("Unknown element type.")

    # Print the operand
    print("output = "+covert_to_string(element))
    
    # Return a dummy value
    return "dummy"


# Function to apply the Order unary operator
def apply_order(cse_machine, operand):
    if isinstance(operand, str):
        return ord(operand[0])
    else:
        cse_machine._error_handler.handle_error("CSE : Invalid unary operation")

# Function to apply the Stern unary operator
def apply_stern(cse_machine, operand):
    if isinstance(operand, str) and len(operand) >= 1:
        return operand[0]
    else:
        cse_machine._error_handler.handle_error("CSE : Invalid unary operation")

def apply_stem(cse_machine, operand):
    if isinstance(operand, str) and len(operand) >= 1:
        return operand[1:]
    else:
        cse_machine._error_handler.handle_error("CSE : Invalid unary operation")