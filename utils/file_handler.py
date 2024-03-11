def read_file_content(file_name):
    """
    Read the content of the specified file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """
    try:
        with open(file_name, "r", encoding='utf-8') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Error: An error occurred while reading the file '{file_name}': {e}")
        return None
