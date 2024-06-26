#rpal_tests/rpal_exe.py

#Description
#This module is used to run the Repl.it Pal (rpal.exe) code analysis tool on the specified source file.

#Usage
#This module is used to run the Repl.it Pal (rpal.exe) code analysis tool on the specified source file.

import os
import subprocess


def rpal_exe(source_file_path, flag=None):
    """
    Runs the Repl.it Pal (rpal.exe) code analysis tool on the specified source file.

    Args:
        source_file_path (str): The path to the source file to analyze.
        ast (bool, optional): Whether to return the Abstract Syntax Tree (AST) of the file.
            Defaults to False.

    Returns:
        Union[List[str], None]: The output of the rpal.exe tool as a list of strings, or None if
            an error occurred. If the AST option is specified, the output will not include the
            final result string.
    """

    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the source file
    source_file_path = os.path.join(current_directory, "rpal_sources", source_file_path)

    # Check if the source file exists
    if not os.path.exists(source_file_path):
        print(f"Error: '{source_file_path}' file not found in the rpal_sources directory.")
        return None

    # Construct the full path to rpal.exe
    rpal_exe_path = os.path.join(current_directory, "rpal.exe")

    # Check if rpal.exe exists
    if not os.path.exists(rpal_exe_path):
        print("Error: rpal.exe not found in the current directory.")
        return None

    """ # Construct the full path to the source file
    source_file_path = os.path.join(current_directory, "rpal_sources", source_file_name)

    # Check if the source file exists
    if not os.path.exists(source_file_path):
        print(f"Error: '{source_file_name}' file not found in the rpal_sources directory.")
        return None """

    # Prepare the command to execute rpal.exe
    command = [rpal_exe_path, source_file_path]
    if flag=="ast":
        command.insert(1, "-ast")
    elif flag == "st" :
        command.insert(1, "-st")

    # Print the command for debugging
    #print("Executing command:", " ".join(command))

    try:
        # Execute the command and capture the output
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        original_output = process.communicate()[0].decode("utf-8")
        
        # If ast is True, exclude the last element (result)
        if flag=="ast":
            original_output = original_output#.splitlines()

        # Print the original output and its raw version
        if flag=="ast":
            print("\nOriginal rpal.exe output:\n", original_output, "\n")
        elif flag=="st":
            print("\nOriginal rpal.exe output:\n", original_output, "\n")
        else:
            print("\nOriginal rpal.exe output\n:", original_output,
                  "raw version:", repr(original_output), "\n",source_file_path)

        return original_output

    except Exception as e:
        print("An error occurred while executing rpal.exe:", e)
        return None

