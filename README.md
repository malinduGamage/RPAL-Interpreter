![Tests](https://github.com/malinduGamage/RPAL-Interpreter/actions/workflows/makefile.yml/badge.svg)

## RPAL-Interpreter

## Table of Contents

- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- - [Lexical Analyzer](#lexical-analyzer)
- - [Screener](#screener)
- - [Parser](#parser)
- - [CSE Machine](#cse-machine)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributors](#contributors)
- [License](#license)

## About

RPAL-Interpreter is a Python package for interpreting RPAL (Recursive Programming Algorithmic Language) code. It provides functionality for lexical analysis, parsing, error handling, and interpretation of RPAL programs.

## Features

- Tokenizes a given RPAL program
- Constructs the Abstract Syntax Tree (AST) and Standard Tree (ST)
- Additional functions to print AST and ST
- Generates Control Structures
- Executes the RPAL program and produces the output

The interpreter consists of the following main components:

## Project Structure

The RPAL interpreter project is structured into several components, each responsible for specific functionalities related to lexical analysis, parsing, interpretation, and error handling. Below is an overview of the project structure and its key components:

## Lexical Analyzer

- The Lexical Analyzer is responsible for scanning the given RPAL program and preparing the token list for the parser. Tokens are categorized according to the RPAL lexical rules.

### Functionality

- Scans the RPAL source file.
- Identifies tokens based on the RPAL lexical rules.
- Outputs a token list, consisting of token objects containing type and value attributes.
  - **Input**: RPAL source file
  - **Output**: token list (list of token objects(type, value))

## Screener

- The Screener is a component that further processes the token list generated by the Lexical Analyzer. It filters the token list based on certain criteria and prepares it for consumption by the parser.

### Functionality

- Filters the token list to remove unnecessary tokens.
- Identifies keywords and categorizes them appropriately.
- Outputs a filtered token list suitable for parsing.
  - **Input**: Token list generated by the Lexical Analyzer
  - **Output**: Filtered token list (list of token objects with attributes: type, value)

## Parser

- The Parser component takes the token list generated by the Lexical Analyzer and constructs both the Abstract Syntax Tree (AST) and Standard Tree (ST) from it.

#### Functionality

- Receives the token list from the Lexical Analyzer.
- Constructs the Abstract Syntax Tree (AST) and Standard Tree (ST) based on the provided tokens.
- Outputs the Standard Tree (ST).
  - **Input**: token list generated by the Screener.
  - **Output**: Standard Tree(ST)

## CSE Machine

- The CSE (Control Structure Environment) Machine performs the evaluation of the RPAL source program by traversing the Standard Tree (ST) in a pre-order manner. It generates control structures and applies the 13 CSE rules to produce the output of the source program.

### Functionality

- Traverses the Standard Tree (ST) in a pre-order manner.
- Generates control structures during traversal.
- Applies the 13 CSE rules to evaluate the source program.
- Produces the output of the source program.
  - **Input**: Standard Tree (ST).
  - **Output**: Output of the source program.

## Usage

To use the RPAL-Interpreter, follow these steps:

1. Install the dependencies by running

```bash
pip install -r requirements.txt
```

2. Write your RPAL code in a file (e.g., `example.rpal`).
3. Run the main script `main.py` with the file name as an argument:

```bash
python main.py example.rpal
```

The following sequence of commands can be used in the root of the project directory to compile the program and execute RPAL programs:

To generate the Abstract Syntax Tree:

```bash
python main.py -ast file_name
```

#### Additional Switches for Analysis (Debugging):

To generate the token list from the lexical analyzer:

```bash
python main.py -t file_name
```

To generate the filtered token list from the screene:

```bash
python main.py -ft file_name
```

To generate the Standardized Tree:

```bash
python main.py -st file_name
```

#### Make Commands (Alternative Method)

Alternatively, you can use the following make commands:  
**Install Dependencies:**

```bash
make install
```

**Run Program (test.txt):**

```bash
make run
```

**Run Tests:**  
All test :

```bash
make test_ast
```

Specific file (in rpal_tests/rpal_source):

```bash
make test_ast F=file_name
```

**All in One (Install, Run, Test):**

```bash
make all
```

#### Note for Windows Users

For Windows users, some commands may require [Cygwin](https://www.cygwin.com/install.html) or similar tools for execution.

## Directory Structure

```bash
RPAL-Interpreter/
|
├── main.py                             # Main entry point of the application
|
├── lexical_analyzer/                   # Package for lexical analysis functionality
│   ├── scanner.py                      # Module containing lexical scanner logic
│   └── __init__.py                     # Marks the directory as a Python package
|
├── screener/                           # Package for screening functionality
│   ├── screener.py                     # Module containing screening logic
│   └── __init__.py                     # Marks the directory as a Python package
|
├── parser/                             # Package for parsing functionality
│   ├── parser_module.py                # Module containing parser logic
│   └── __init__.py                     # Marks the directory as a Python package
|
├── interpreter/                        # Package for interpreter functionality
│   ├── execution_engine.py             # Module containing interpreter logic
│   └── __init__.py                     # Marks the directory as a Python package
|
├── error_handling/                     # Package for error handling functionality
│   ├── error_handler.py                # Module containing error handling logic
│   └── __init__.py                     # Marks the directory as a Python package
|
├── table_routines/                     # Package for table routines functionality
│   ├── char_map.py                     # Module containing character mapping logic
│   ├── fsa_table.py                    # Module containing Finite State Automaton table logic
│   ├── accept_states.py                # Module containing accept states logic
│   ├── keywords.py                     # Module containing keywords set
│   └── __init__.py                     # Marks the directory as a Python package
|
├── utils/                              # Package for utility functionalities
│   ├── tokens.py                       # Module containing token class definition
│   ├── node.py                         # Module containing node data structure class definition
│   ├── stack.py                        # Module containing stack class definition
│   ├── token_printer.py                # Module containing token printing function (for debugging purposes)
│   ├── AST_printer.py                  # Module containing AST printing function (for debugging purposes)
│   ├── AST_list.py                     # Module for listing AST
│   ├── test_program.py                 # List of program file names in rpal_tests/rpal_source
│   ├── file_handler.py                 # Module containing file handling functions
│   └── __init__.py                     # Marks the directory as a Python package
|
├── rpal_tests/                         # Directory for tests
│   ├── rpal_sources/                   # Directory for RPAL source code files to test
│   ├── test_generate_tests.py          # Module for generating tests
│   ├── test_generate_ast_tests.py      # Module for generating tests in rpal_source by pytest
│   ├── assert_program                  # Module
│   ├── rpal_exe.py                     # Module for executing RPAL source code
│   ├── rpal_interpret.py               # Module for interpreting RPAL source code
│   ├── cygwin1.dll                     # Cygwin DLL required for execution (if applicable)
│   └── __init__.py                     # Marks the directory as a Python package
|
├── doc/                                # Directory for documentation files
|
├── .vscode/                            # Directory for VS Code settings
│   └── settings.json                   # VS Code settings file
|
├── requirements.txt                    # File containing project dependencies
|
├── Makefile                            # Makefile for automating tasks such as installation, running tests, and cleaning up
|
└── __init__.py                         # Marks the directory as a Python package



```

This directory structure outlines the organization of your RPAL interpreter project, with each package and module serving a specific purpose related to lexical analysis, parsing, interpretation, error handling, table routines, and utilities.

For more detailed information about the purpose of each file and the function prototypes along with their uses, please refer to the [documentation](https://docs.google.com/document/d/1knA2_kh6vq_9lilMKiYFS5hVSPmpnmvaV6-6ir3mjp8/edit).

## Contributors

- Fernando T.H.L (@[uchihaIthachi](https://github.com/UchihaIthachi))
- Malindu Gamage (@[malinduGamage](https://github.com/malinduGamage))

## License

This project is licensed under the MIT License - see the LICENSE file for details.
