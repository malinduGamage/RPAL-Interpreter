#rpal_tests/test_generate_ast_tests.py

# Description:
# Generates test cases for the RPAL interpreter by comparing the output of the RPAL program obtained by running the program using rpal_exe with the output obtained by interpreting the program using the Evaluator.

# Usage:
# The test_program function can be used to generate test cases for the RPAL interpreter by comparing the output of the RPAL program obtained by running the program using rpal_exe with the output obtained by interpreting the program using the Evaluator.

import pytest
from rpal_tests.assert_program import program
from utils.test_program import test_programs

"""
This function is a test function that is used to test the functionality of the interpreter.

Args:
    program_name (str): The name of the program to be tested.

Returns:
    tuple: A tuple containing the actual and original program strings.

"""

# Parametrize the test cases dynamically

@pytest.mark.parametrize("program_name", test_programs)
def test_program(program_name):
    actual_program ,original_program = program(program_name,True)
    assert actual_program == original_program
    