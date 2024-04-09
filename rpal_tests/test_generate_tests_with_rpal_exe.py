#rpal_tests/test_generate_ast_tests.py

# Description:
# Generates test cases for the RPAL interpreter by comparing the output of the RPAL program obtained by running the program using rpal_exe with the output obtained by interpreting the program using the Evaluator.

# Usage:
# The test_program function can be used to generate test cases for the RPAL interpreter by comparing the output of the RPAL program obtained by running the program using rpal_exe with the output obtained by interpreting the program using the Evaluator.

import pytest
import time
from rpal_tests.assert_program import program 
from rpal_tests.program_name_list import test_programs

# Fixture to add a delay between test cases
@pytest.fixture(scope="function", autouse=True)
def delay_between_test_cases():
    # Wait for 1 second between test cases
    time.sleep(0)

# Parametrize the test cases dynamically
@pytest.mark.parametrize("program_name", test_programs)
def test_program(program_name):
    actual_program ,original_program = program(program_name)
    assert actual_program == original_program




    