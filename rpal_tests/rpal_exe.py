import os
import subprocess

def rpal_exe(source_file_path, ast=False):
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
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
    if ast:
        command.insert(1, "-ast")

    # Print the command for debugging
    print("Executing command:", " ".join(command))

    try:
        # Execute the command and capture the output
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        original_output = process.communicate()[0].decode("utf-8")

        

        # If ast is True, exclude the last element (result)
        if ast:
            original_output = original_output.split()[:-1]
        
        # Print the original output and its raw version
        if ast :
            print("\nOriginal rpal.exe output:\n", original_output,"\n")
        else :
            print("\nOriginal rpal.exe output\n:", original_output, "raw version:", repr(original_output),"\n")
        
        return original_output
    
    except Exception as e:
        print("An error occurred while executing rpal.exe:", e)
        return None

# Test the rpal.exe
if __name__ == "__main__":
    current_file_name = os.path.basename(__file__)
    rpal_exe(current_file_name)
