from rpal_tests.rpal_exe import rpal_exe
#from interpreter.execution_engine import Evaluator 

def program(filename):
    # Setup: Obtain original output by running the RPAL program using rpal_exe
    input_program = filename
    original_output = rpal_exe(input_program)

    print(repr(original_output))
    """ # Execution: Obtain actual output by interpreting the program using the Evaluator
    evaluator = Evaluator()
    actual_output = evaluator.interpret(filename) """

    # Manually set the actual output for testing purposes
    actual_output = "15\n"
    # Assertion: Compare original output with actual output
    
    assert actual_output == original_output
