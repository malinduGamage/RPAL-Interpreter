
def var_lookup(cse_machine , var_name):
    env_pointer = cse_machine.current_env
    while env_pointer.parent:
        if var_name in env_pointer._environment:
            out = env_pointer._environment[var_name]
            if out[0] == 'eta':
                print(var_name,f"['eta',η_{out[1].control_structure}{out[1].bounded_variable}]")
            else:
                print(var_name,out)
            return out
        env_pointer = env_pointer.parent
    else:
        cse_machine._error_handler.handle_error(f"CSE : Variable [{var_name}] not found in the environment")

def add_table_data(cse_machine,rule):
    table_data = cse_machine.table_data
    table_data.append((rule,cse_machine.control.whole_stack()[:],cse_machine.stack.whole_stack()[:],[cse_machine.current_env.index][:]))

def print_cse_table(cse_machine):
    table_data = cse_machine.table_data
    cse_machine._add_table_data("")
    control_width = 60
    stack_width = 55
    total_width = control_width + stack_width + 16
    print("\nCSE TABLE")
    print("\nRULE | CONTROL" +  " " * (control_width-6) + "|"+" "*(stack_width-5)+" STACK " + "| ENV")
    print("-" * total_width)
    for data in table_data:
        rule = f"{data[0]:<2} |"
        control = " ".join(str(element_val(element)) for element in data[1])
        stack = " ".join(str(element_val(element)) for element in data[2][::-1])
        env = f" {data[-1][0]}"
        
        control_str = f"{control[:control_width]:<{control_width}}"
        stack_str = f"{stack[:stack_width]:>{stack_width}}"
        
        print(f"  {rule} {control_str} | {stack_str} | {env}")
        print("-" * total_width )
        
def element_val(element):
    if element.type == "tuple":
        output = []
        for el in element.value:
            output.append(el.value)
        return output
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