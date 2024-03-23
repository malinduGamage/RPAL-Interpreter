def read_file_content(file_name):
    """
    Read the content of the specified file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """
    try:
        # Attempt to open the file in read mode and read its content

        with open(file_name, "r", encoding='utf-8') as file:
            file_content = file.read()
        return file_content    # Return the content of the file if successful
    
    except FileNotFoundError:
        # Print an error message if the file is not found

        print(f"Error: File '{file_name}' not found.")
        return None    # Return None to indicate an error occurred
    
    except Exception as e:
        # Print an error message for any other exceptions that occur during file reading
        
        print(f"Error: An error occurred while reading the file '{file_name}': {e}")
        return None   # Return None to indicate an error occurred
