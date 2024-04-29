####################################################################################################
# cse machine helpers functions
####################################################################################################
def var_lookup(cse_machine , var_name):
    """
    Searches the current environment for a variable with the given name.

    Args:
        cse_machine (CSE_Machine): The CSE machine that is currently running.
        var_name (str): The name of the variable to search for.

    Returns:
        Any: The value of the variable, or None if the variable was not found.

    Raises:
        CSEError: If the variable was not found and no default value was provided.
    """
    env_pointer = cse_machine.current_enviroment
    while env_pointer:
        if var_name in env_pointer._environment:
            out = env_pointer._environment[var_name]
            return out
        env_pointer = env_pointer.parent
    else:
        cse_machine._error_handler.handle_error(f"CSE : Variable [{var_name}] not found in the environment")

####################################################################################################
# Printer helper functions
################################################################################################
    
def convert_list(element,out):
    """Convert a list to a string.

    Args:
        element (list): The list to convert.
        out (str): The string to append the converted list to.

    Returns:
        str: The string with the converted list appended to it.
    """
    if isinstance(element, list):
        out += "("
        for el in element:
            out = convert_list(el,out)
        out = out[:-1] +  ")"
    else:
        if isinstance(element.value, list):
            out += "("
            for el in element.value:
                out = convert_list(el,out)
            out = out[:-1] +  "),"
        else:
            out += str(element.value) + ","
    return out

def raw(string):
    return string.encode('unicode_escape').decode()

################################################################################################
# cse table functions
################################################################################################

import functools

def add_table_data(cse_machine,rule):
    """Add the given rule to the CSE table.

    Args:
        cse_machine (CSE_Machine): The CSE machine that is currently running.
        rule (Rule): The rule to add to the table.
    """
    table_data = cse_machine.table_data
    table_data.append((rule,cse_machine.control.whole_stack()[:],cse_machine.stack.whole_stack()[:],[cse_machine.current_enviroment.index][:]))

def add_table_data_decorator(table_entry):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            self._add_table_data(table_entry)
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def print_cse_table(cse_machine):
    """Print the CSE table.

    Args:
        cse_machine (CSE_Machine): The CSE machine that is currently running.
    """
    table_data = cse_machine.table_data
    cse_machine._add_table_data("")
    control_width = 80
    stack_width = 60
    total_width = control_width + stack_width + 16
    print("\nCSE TABLE")
    print("\nRULE | CONTROL" +  " " * (control_width-6) + "|"+" "*(stack_width-5)+" STACK " + "| ENV")
    print("-" * total_width)
    for data in table_data:
        rule = f"{data[0]:<2} |"
        control = " ".join(str(element_val(element)) for element in data[1])
        stack = " ".join(str(element_val(element)) for element in data[2][::-1])
        env = f" {data[-1][0]}"
        l = len(control)
        control_str = f"{control[max(0, l - control_width):]:<{control_width}}"
        stack_str = f"{stack[:stack_width]:>{stack_width}}"
        
        print(f"  {rule} {control_str} | {stack_str} | {env}")
        print("-" * total_width )
        

################################################################################################
# helper functions for cse table
################################################################################################
        
def element_val(element):
    """Get the value of a given element.

    Args:
        element (Element): The element to get the value of.

    Returns:
        Any: The value of the element.
    """
    if element.type == "tuple":
        output = ""
        return convert_list(element.value,output)
    elif element.type == "env_marker":
        return f"e{element.env.index}"
    elif element.type == "lambda":
        return f"λ_{element.control_structure}{element.bounded_variable}"
    elif element.type == "delta":
        return f"δ_{element.control_structure}"
    elif element.type == "gamma":
        return "γ"
    elif element.type == "beta":
        return "β"
    elif element.type == "eta":
        return f"η_{element.control_structure}[{element.bounded_variable}]"
    elif element.type == "tau":
        return f"tau[{element.value}]"
    else:
        return element.value 