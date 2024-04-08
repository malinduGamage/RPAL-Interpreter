def apply_unary(cse_machine, rator, unop):
    # Dictionary mapping binary operators to their corresponding functions
    unary_operators = {
            "Print": lambda cse_machine, operand: apply_print(cse_machine, operand),
            "Isstring": lambda cse_machine, operand: isinstance(operand, str),
            "Isinteger": lambda cse_machine, operand: isinstance(operand, int),
            "Istruthvalue": lambda cse_machine, operand: isinstance(operand, bool),
            "Isfunction": lambda cse_machine, operand: callable(operand),
            "Null": lambda cse_machine, operand: operand is None,
            "Istuple": lambda cse_machine, operand: isinstance(operand, tuple),
            "Order": lambda cse_machine, operand: apply_order(cse_machine, operand),
            "Stern": lambda cse_machine, operand: apply_stern(cse_machine, operand),
            "Stem": lambda cse_machine, operand: apply_stem(cse_machine, operand),
            "ItoS": lambda cse_machine, operand: str(operand),
            "neg": lambda cse_machine, operand: -operand if isinstance(operand, int) else cse_machine._error_handler.handle_error("CSE : Invalid unary operation"),
            "not": lambda cse_machine, operand: not operand if isinstance(operand, bool) else cse_machine._error_handler.handle_error("CSE : Invalid unary operation"),
            "$ConcPartial": lambda cse_machine, operand: cse_machine._error_handler.handle_error("CSE : Not implemented")
        }
    # Get the operation function corresponding to the binary operator
    operation_function = unary_operators.get(unop)
    if operation_function:
        # Apply the operation function with the provided operands
        return operation_function(cse_machine, rator)
    else:
        # If the binary operator is not recognized, raise an error
        raise ValueError("Invalid binary operation: " + unop)

# Function to apply the Print unary operator
def apply_print(cse_machine, operand):
    print(operand)
    return operand

# Function to apply the Order unary operator
def apply_order(cse_machine, operand):
    if isinstance(operand, str):
        return ord(operand[0])
    else:
        cse_machine._error_handler.handle_error("CSE : Invalid unary operation")

# Function to apply the Stern unary operator
def apply_stern(cse_machine, operand):
    if isinstance(operand, tuple) and len(operand) >= 1:
        return operand[-1]
    else:
        cse_machine._error_handler.handle_error("CSE : Invalid unary operation")

def apply_stem(cse_machine, operand):
    if isinstance(operand, tuple) and len(operand) >= 1:
        return operand[:-1]
    else:
        cse_machine._error_handler.handle_error("CSE : Invalid unary operation")