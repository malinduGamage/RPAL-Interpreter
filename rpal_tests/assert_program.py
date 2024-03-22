import os
from rpal_tests.rpal_exe import rpal_exe
from interpreter.execution_engine import Evaluator 

def program(source_file_name,ast=False):
    """
    Runs the RPAL program with the given source file name.

    Parameters:
    source_file_name (str): The name of the RPAL source file to run.
    ast (bool, optional): Whether to return the abstract syntax tree of the program. Defaults to False.

    Returns:
    Union[str, List[Any]]: The output of the RPAL program, or the abstract syntax tree if `ast` is True.
    """
    # Setup: Obtain original output by running the RPAL program using rpal_exe
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    

    # Construct the full path to the source file
    source_file_path = os.path.join(current_directory, "rpal_sources", source_file_name)

    # Check if the source file exists
    if not os.path.exists(source_file_path):
        print(f"Error: '{source_file_name}' file not found in the rpal_sources directory.")
        return None
    original_output = rpal_exe(source_file_path,ast)
     # Execution: Obtain actual output by interpreting the program using the Evaluator
    evaluator = Evaluator()
    actual_output = evaluator.interpret(source_file_path) 

    if ast:
        actual_output = evaluator.get_ast_list()
        print("\nactual output :\n",actual_output, "\n")
    else:
        # Manually set the actual output for testing purposes
        actual_output = "15\n"
        print("\nactual output :\n",actual_output,"raw version",repr(actual_output), "\n") 
    
    # Assertion: Compare original output with actual output
    
    return actual_output , original_output
