# RPAL-Interpreter

# RPAL-Interpreter

RPAL-Interpreter is a Python package for interpreting RPAL (Recursive Porgramming Algorithmic Language) code. It provides functionality for lexical analysis, parsing, error handling, and interpretation of RPAL programs.

## Project Structure

RPAL-Interpreter/
├── init.py # Marks the directory as a Python package
├── main.py # Main entry point of the application
├── requirements.txt # File containing project dependencies
├── doc/ # Directory for documentation files
├── .vscode/ # Directory for VS Code settings
│ └── settings.json # VS Code settings file
├── error_handling/ # Package for error handling functionality
│ ├── init.py # Marks the directory as a Python package
│ └── error_handler.py # Module containing error handling logic
├── lexical_analyzer/ # Package for lexical analysis functionality
│ ├── init.py # Marks the directory as a Python package
│ └── scanner.py # Module containing lexical scanner logic
├── table_routines/ # Package for table routines functionality
│ ├── init.py # Marks the directory as a Python package
│ ├── char_map.py # Module containing character mapping logic
│ ├── fsa_table.py # Module containing Finite State Automaton table logic
│ └── accept_states.py # Module containing accept states logic
├── parser/ # Package for parsing functionality
│ ├── init.py # Marks the directory as a Python package
│ └── parser.py # Module containing parser logic
├── screener/ # Package for screening functionality
│ ├── init.py # Marks the directory as a Python package
│ └── screener.py # Module containing screening logic
├── interpreter/ # Package for interpreter functionality
│ ├── init.py # Marks the directory as a Python package
│ └── execution_engine.py# Module containing interpreter logic
└── utils/ # Package for utility functionalities
├── init.py # Marks the directory as a Python package
├── tokens.py # Module containing token class definition
├── token_printer.py # Module containing token printing function
└── file_handler.py # Module containing file handling functions

## Usage

To use the RPAL-Interpreter, follow these steps:

1. Install the dependencies by running `pip install -r requirements.txt`.
2. Write your RPAL code in a file (e.g., `example.rpal`).
3. Run the main script `main.py` with the file name as an argument: `python main.py example.rpal`.

## Contributors

- John Doe (@johndoe)
- Jane Smith (@janesmith)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
