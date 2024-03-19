import os
import subprocess

def rpal_exe(source_file_name):
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full path to rpal.exe
    rpal_exe_path = os.path.join(current_directory, "rpal.exe")

    # Check if rpal.exe exists
    if not os.path.exists(rpal_exe_path):
        print("Error: rpal.exe not found in the tests directory.")
        return

    # Construct the full path to the source file
    source_file_path = os.path.join(current_directory, "rpal_sources", source_file_name)

    # Check if the source file exists
    if not os.path.exists(source_file_path):
        print(f"Error: '{source_file_name}' file not found in the rpal_sources directory.")
        return

    # Run the original rpal.exe interpreter
    process = subprocess.Popen([rpal_exe_path, source_file_path], stdout=subprocess.PIPE)
    original_output = process.communicate()[0].decode("utf-8")

    print("Original rpal.exe output:", original_output, "raw version:", repr(original_output))
    
    return original_output

# Test the rpal.exe
if __name__ == "__main__":
    current_file_name = os.path.basename(__file__)
    execute(current_file_name)
