![Tests](https://github.com/malinduGamage/RPAL-Interpreter/actions/workflows/testing.yml/badge.svg)

## RPAL-Interpreter

- This project was the culmination of the CS3513-Programming Languages module, which was part of the curriculum offered by the Department of Computer Science & Engineering at the University of Moratuwa. It was completed during the 4th semester of Batch 21.

## Table of Contents

- [Problem Requirements](#problem-requirements)
- [About our solution](#about-our-solution)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
  - [Lexical Analyzer](#lexical-analyzer)
  - [Screener](#screener)
  - [Parser](#parser)
  - [CSE Machine](#cse-machine)
- [Project Structure](#project-structure)
- [Contributors](#contributors)
- [License](#license)

## Problem Requirements

- Implement a lexical analyzer and a parser for the RPAL (Right-reference Pedagogic Algorithmic Language). Refer the [RPAL_Lex](https://github.com/malinduGamage/RPAL-Interpreter/blob/main/doc/RPAL_Lex.pdf) for the lexical rules and [RPAL_Grammar](https://github.com/malinduGamage/RPAL-Interpreter/blob/main/doc/RPAL_Grammar.pdf) for the grammar details.Additionally, refer to [About RPAL](https://github.com/malinduGamage/RPAL-Interpreter/blob/main/doc/About%20RPAL.pdf) for information about the RPAL language.
- The output of the parser should be the Abstract Syntax Tree (AST) for the given input program.
  Implement an algorithm to convert the Abstract Syntax Tree (AST) in to Standardize Tree (ST) and implement CSE machine.Refer to the [semantics](https://github.com/malinduGamage/RPAL-Interpreter/blob/main/doc/semantics.pdf) document, which contains the rules for transforming the AST into the ST
- Program should be able to read an input file which contains a RPAL program and return Output which should match the output of rpal.exe for the relevant program.
- For more details, refer the [Project_Requirements](https://github.com/malinduGamage/RPAL-Interpreter/blob/main/doc/ProgrammingProject.pdf) document.

## About our solution

- **Programming Language**:python
- **Development & Testing**: Visual Studio Code, Command Line, Cygwin, Pytest, GitHub Actions

## Usage

To use the RPAL-Interpreter, follow these steps:

> ### Prerequisites
>
> Your local machine must have Python and pip installed.

1. Clone the repository to your local machine or download the project source code as a ZIP file.
2. Navigate to the root directory of the project in the command line interface.
3. Install the dependencies by running the following command in the project directory:

```bash
pip install -r requirements.txt
```

4. Put your RPAL test programs in the root directory. We had added the [test.txt](https://github.com/malinduGamage/RPAL-Interpreter/blob/main/test.txt) to the root directory, which contains the sample input program of the [Project_Requirements](https://github.com/malinduGamage/RPAL-Interpreter/blob/main/doc/ProgrammingProject.pdf) document.
   Run the main script `main.py` with the file name as an argument:

```bash
python main.py file_name
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

To generate the filtered token list from the screen:

```bash
python main.py -ft file_name
```

To generate the Standardized Tree:

```bash
python main.py -st file_name
```

To generate the CSE table:

```bash
python main.py -ct file_name
```

#### Using Make Commands (Alternative Method)

**Your local machine must be able to run make command**

> #### Note for Windows Users

> For Windows users, for make commad [Cygwin](https://www.cygwin.com/install.html) or similar unix like env tools for execution.

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
Run all tests (in rpal_tests/rpal_sources/) :

```bash
make test_all
```

Run tests for final result (in rpal_tests/rpal_sources/) :

```bash
make test
```

Run tests for AST result (in rpal_tests/rpal_sources/):

```bash
make test_ast
```

Run tests for ST result (in rpal_tests/rpal_sources/):

```bash
make test_st
```

**All in One (Install, Run, Test(test_all)):**

```bash
make all
```

> #### Note for Python 3 Users
>
> If you have both Python 2 and Python 3 installed, you may need to use python3 instead of python in the commands above. Similarly, use pip3 instead of pip for installing packages.

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

## Directory Structure

```bash
RPAL-Interpreter/
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
│   ├── build_standard_tree.py          # Module for converting AST to standard tree
│   ├── parser_module.py                # Module containing parser logic (filter token to AST)
│   └── __init__.py                     # Marks the directory as a Python package
|
├── cse_machine/                        # Package for parsing functionality
│   ├── apply_operations/
│   │   ├── apply_bi.py
│   │   ├── apply_un.py
│   │   └── __init__.py                 # Marks the directory as a Python package
│   ├── data_structures/
│   │   ├── enviroment.py
│   │   ├── stack.py
│   │   ├── control_structure.py
│   │   └── __init__.py
│   ├── utils/
│   │   ├── STlinearlizer.py
│   │   ├── util.py
│   │   └── __init__.py                 # Marks the directory as a Python package
│   ├── machine.py
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
│   ├── tree_printer.py                 # Module containing tree printing function (for debugging purposes)
│   ├── tree_list.py                    # Module for listing tree elements
│   ├── file_handler.py                 # Module containing file handling functions
│   └── __init__.py                     # Marks the directory as a Python package
|
├── rpal_tests/                         # Directory for tests
│   ├── rpal_sources/                   # Directory for RPAL source code files to test
│   ├── test_generate_tests.py          # Module for generating tests
│   ├── test_generate_ast_tests.py      # Module for generating tests in rpal_sources by pytest for AST
│   ├── test_generate_st_tests.py       # Module for generating tests in rpal_sources by pytest for standard tree
│   ├── test_generate_tests_with_rpal_exe.py      # Module for generating tests in rpal_sources by pytest output generated by real rpal.exe
│   ├── test_generate_ast_tests_with_rpal_exe.py  # Module for generating tests in rpal_sources by pytest for AST output generated by real rpal.exe
│   ├── test_generate_st_tests_with_rpal_exe.py   # Module for generating tests in rpal_sources by pytest for standard tree output generated by real rpal.exe
│   ├── assert_program .py              # Module for checking tests
│   ├── program_name_list.py            # List of program names in rpal_sources directory
│   ├── output.py                       # List of outputs generated by rpal.exe
│   ├── output_ast.py                   # List of AST outputs generated by rpal.exe
│   ├── output_st.py                    # List of standard tree outputs generated by rpal.exe
│   ├── rpal.exe                        # RPAL interpreter
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
