# parser/__init__.py

# Description:
# This package contains modules related to parsing RPAL code and constructing Abstract Syntax Trees (ASTs).

# parser/parser_module.py

# Description:
# This module contains the Parser class, which is responsible for parsing the input code and constructing an Abstract Syntax Tree (AST).
# The parser utilizes a recursive descent parsing technique to analyze the structure of the input code based on predefined grammar rules outlined in the "RPAL_Grammar.pdf" document in the doc directory.
# It identifies expressions, definitions, variables, and other language constructs, and builds a hierarchical representation of the code in the form of an AST.

# Usage:
# To use the Parser class, create an instance of the class. The Parser class provides the `parse()` method, which takes a list of tokens as input.
# Call the `parse()` method with the list of tokens representing the code to be parsed. The parser will analyze the code and construct an AST accordingly.
# Once parsing is complete, the status attribute of the Parser instance will indicate whether parsing was successful.
# The constructed AST can be accessed using the stack attribute of the Parser instance.

# parser/build_standard_tree.py

# Description:
# This module contains the StandardTree class, which is used to build a standard tree from a given AST tree. 
# The standard tree is a transformed version of the input tree based on predefined rules and transformations outlined in the "semantics.pdf" documentation.

# Usage:
# This module provides the StandardTree class, which can be utilized to transform an input tree into a standard form.
# The build_standard_tree method applies a series of transformations to the input tree, resulting in a standard tree.
# Each transformation corresponds to specific cases or patterns found in the input tree's structure.
