#rpal_tests/assert_program.py

# Description:
# This function is used to compare the output of the RPAL program obtained by running the program using rpal_exe with the output obtained by interpreting the program using the Evaluator.

#Usage:
# The program function can be used to compare the output of the RPAL program obtained by running the program using rpal_exe with the output obtained by interpreting the program using the Evaluator.

import os
from rpal_tests.rpal_exe import rpal_exe
from interpreter.execution_engine import Evaluator 

def program(source_file_name,flag=None):
    # Setup: Obtain original output by running the RPAL program using rpal_exe
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    

    # Construct the full path to the source file
    source_file_path = os.path.join(current_directory, "rpal_sources", source_file_name)

    # Check if the source file exists
    if not os.path.exists(source_file_path):
        print(f"Error: '{source_file_name}' file not found in the rpal_sources directory.")
        return None
    output = rpal_exe(source_file_path)
    if flag != None:
        original_output = rpal_exe(source_file_path,flag)
    else :
        original_output = output

     # Execution: Obtain actual output by interpreting the program using the Evaluator
    evaluator = Evaluator()
    evaluator.interpret(source_file_path) 

    if flag == "ast":
        actual_output = "\n".join(evaluator.get_ast_list())
        actual_output += ("\n"+output)
        print("\nactual output :\n",actual_output, "\n")
    elif flag == "st":
        actual_output = "\n".join(evaluator.get_st_list())
        actual_output += ("\n"+output)
        print("\nactual output :\n",actual_output, "\n")
    else:
        # Manually set the actual output for testing purposes
        actual_output = evaluator.get_output()
        evaluator.print_cse_table()
        print("\nactual output :\n",actual_output,"raw version",repr(actual_output), "\n") 
    
    # Assertion: Compare original output with actual output
    return actual_output , original_output
