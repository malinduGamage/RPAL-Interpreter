
def var_lookup(cse_machine , var_name):
    env_pointer = cse_machine.current_env
    while env_pointer.parent != None:
        if var_name in env_pointer._environment:
            
            print(var_name,env_pointer._environment[var_name],"==========================")
            return env_pointer._environment[var_name]
        env_pointer = env_pointer.parent
    else:
        cse_machine._error_handler.handle_error("CSE : Variable not found in the environment")

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
        control = " ".join(str(element.value) for element in data[1])
        stack = " ".join(str(element.value) for element in data[2][::-1])
        env = f" {data[-1][0]}"
        
        control_str = f"{control[:control_width]:<{control_width}}"
        stack_str = f"{stack[:stack_width]:>{stack_width}}"
        
        print(f"  {rule} {control_str} | {stack_str} | {env}")
        print("-" * total_width )