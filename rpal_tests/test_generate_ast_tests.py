import pytest
from rpal_tests.assert_program import program
import os
from rpal_tests.rpal_exe import rpal_exe
from interpreter.execution_engine import Evaluator
from utils.test_program import test_programs

# Parametrize the test cases dynamically

@pytest.mark.parametrize("program_name", test_programs)
def test_program(program_name):
    actual_program ,original_program = program(program_name,True)
    assert actual_program == original_program
    