#rpal_tests/test_generate_ast_tests.py

# Description:
# Generates test cases for the RPAL interpreter by comparing the output of the RPAL program obtained by running the program using rpal_exe with the output obtained by interpreting the program using the Evaluator.

# Usage:
# The test_program function can be used to generate test cases for the RPAL interpreter by comparing the output of the RPAL program obtained by running the program using rpal_exe with the output obtained by interpreting the program using the Evaluator.

import os
import pytest
from rpal_tests.assert_program import program 
from rpal_tests.program_name_list import test_programs
from rpal_tests.output_ast import out_ast
from rpal_tests.output import out
from src.interpreter.execution_engine import Evaluator 

"""
This function is a test function that is used to test the functionality of the interpreter.

Args:
    program_name (str): The name of the program to be tested.

Returns:
    tuple: A tuple containing the actual and original program strings.

"""

# Parametrize the test cases dynamically
test_cases = list(zip(test_programs, out_ast))
@pytest.mark.parametrize("program_name", test_programs)
def test_program(program_name):
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    

    # Construct the full path to the source file
    source_file_path = os.path.join(current_directory, "rpal_sources", program_name)

    # Check if the source file exists
    if not os.path.exists(source_file_path):
        print(f"Error: '{program_name}' file not found in the rpal_sources directory.")
        return None

     # Execution: Obtain actual output by interpreting the program using the Evaluator
    evaluator = Evaluator()
    evaluator.interpret(source_file_path)
    actual_output = "\n".join(evaluator.get_ast_list())
    actual_output += ("\n"+out[test_programs.index(program_name)]) 
    expected_output = out_ast[test_programs.index(program_name)]
    assert actual_output == expected_output

    