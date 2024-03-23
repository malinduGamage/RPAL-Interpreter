# parser/parser_module.py

# Description:
# This module contains the Parser class, which is responsible for parsing the input code and constructing an Abstract Syntax Tree (AST).
# The parser utilizes a recursive descent parsing technique to analyze the structure of the input code based on predefined grammar rules.
# It identifies expressions, definitions, variables, and other language constructs, and builds a hierarchical representation of the code in the form of an AST.

# Usage:
# To use the Parser class, create an instance of the class. The Parser class provides the `parse()` method, which takes a list of tokens as input.
# Call the `parse()` method with the list of tokens representing the code to be parsed. The parser will analyze the code and construct an AST accordingly.
# Once parsing is complete, the status attribute of the Parser instance will indicate whether parsing was successful.
# The constructed AST can be accessed using the stack attribute of the Parser instance.

from utils.node import Node
from utils.stack import Stack
from errors_handling.error_handler import ErrorHandler


class Parser:
    """
    Parser class responsible for parsing the input code and constructing an Abstract Syntax Tree (AST).

    This class utilizes a recursive descent parsing technique to analyze the structure of the input code based on predefined grammar rules.
    It identifies expressions, definitions, variables, and other language constructs, and builds a hierarchical representation of the code in the form of an AST.

    Attributes:
        stack (Stack): A stack data structure used to build and manipulate the nodes of the AST during parsing.
        status (bool): Indicates whether parsing was successful. Set to True if parsing completes without errors, otherwise False.

    Methods:
        parse(token_list): Entry point of the recursive descent parser. Parses the list of tokens into an AST.
    """
    def __init__(self):
        """
        Initialize the Parser class by creating a stack and setting the status to False
        """
        self.stack = Stack()
        self.status = False

    #   recursive descent parser
    def parse(self, token_list):
        """
        This function is the entry point of the recursive descent parser. It takes a list of tokens as input and
        attempts to parse them into an AST.

        Args:
            token_list (list): A list of tokens to be parsed

        Returns:
            None
        """
        next_token = token_list.pop(0)

        # function to build the tree
        def build_tree(token, n):
            """
            This function is used to build the tree while parsing. It takes a token and the number of children
            of the node as input and adds the children to the node accordingly.

            Args:
                token (str): The token of the node
                n (int): The number of children of the node

            Returns:
                None
            """
            node = Node(token)
            if self.stack.size() >= n:
                for i in range(n):
                    node.add_child(self.stack.pop())
                self.stack.push(node)
            else:
                ErrorHandler.handle_error(
                    "PARSER : Stack size is less than {n} , cannot create node {token}")

        # function to read a token and update to next_token
        def readToken():
            """
            This function is used to read the next token from the input list and update the next_token variable.

            Returns:
                None
            """
            nonlocal next_token
            if next_token.type in {"ID", "INT", "STR"}:
                build_tree(f"<{next_token.type}:{next_token.value}>", 0)
            if token_list:
                next_token = token_list.pop(0)

        # Expressions ############################################

        # E -> ’let’ D ’in’ E   => ’let’
        #   -> ’fn’ Vb+ ’.’ E   => ’lambda’
        #   -> Ew;

        def E():
            """
            This function is used to parse the expressions in the input code. It can parse a let expression, a
            function expression, or a where expression.

            Returns:
                None
            """
            if next_token.value == "let":
                readToken()
                D()
                if next_token.value == "in":
                    readToken()
                    E()
                    build_tree("let", 2)
                else:
                    ErrorHandler.handle_error("PARSER : Expected 'in' ")

            elif next_token.value == "fn":
                readToken()
                n = 0
                while True:
                    Vb()
                    n += 1
                    if next_token.type not in {"INDETIFIER", "("}:
                        break

                if next_token.value == ".":
                    readToken()
                    E()
                    build_tree("lambda", n+1)
                else:
                    ErrorHandler.handle_error("PARSER : Expected '.' ")
            else:
                Ew()

        # Ew -> T ’where’ Dr    => ’where’
        #    -> T;

        def Ew():
            """
            This function is used to parse the where expressions in the input code. It can parse a tuple
            expression or a regular expression.

            Returns:
                None
            """
            T()
            if next_token.value == "where":
                readToken()
                Dr()
                build_tree("where", 2)

        ## Tuple Expressions ######################################
        # T -> Ta ( ’,’ Ta )+    => ’tau’
        #   -> Ta ;

        def T():
            """
            This function is used to parse the tuple expressions in the input code. It can parse a tuple of
            arbitrary length.

            Returns:
                None
            """
            Ta()
            n = 0
            while next_token.value == ",":
                readToken()
                Ta()
                n += 1
            if n > 0:
                build_tree("tau", n+1)

        # Ta -> Ta ’aug’ Tc      => ’aug’
        #    -> Tc ;

        def Ta():
            """
            This function is used to parse the augmented tuple expressions in the input code. It can parse a
            tuple expression followed by an augment operator.

            Returns:
                None
            """
            Tc()
            while next_token.value == "aug":
                readToken()
                Tc()
                build_tree("aug", 2)

        # Tc -> B ’->’ Tc ’|’ Tc     => ’->’
        #    -> B ;

        def Tc():
            """
            This function is used to parse the conditional tuple expressions in the input code. It can parse a
            boolean expression followed by a conditional operator.

            Returns:
                None
            """
            B()
            if next_token.value == "->":
                readToken()
                Tc()
                if next_token.value == "|":
                    readToken()
                    Tc()
                    build_tree("->", 3)
                else:
                    ErrorHandler.handle_error("PARSER : Expected '|' ")

        ## Boolean Expressions ####################################

        # B -> B ’or’ Bt    => ’or’
        #   -> Bt ;

        def B():
            """
            This function is used to parse the boolean expressions in the input code. It can parse a boolean
            expression followed by an OR operator.

            Returns:
                None
            """
            Bt()
            while next_token.value == "or":
                readToken()
                Bt()
                build_tree("or", 2)

        # Bt -> Bt ’&’ Bs   => ’&’
        #    -> Bs ;

        def Bt():
            """
            This function is used to parse the boolean expressions in the input code. It can parse a boolean
            expression followed by an AND operator.

            Returns:
                None
            """
            Bs()
            while next_token.value == "&":
                readToken()
                Bs()
                build_tree("&", 2)

        # Bs -> ’not’ Bp => ’not’
        #    -> Bp ;

        def Bs():
            """
            This function is used to parse the boolean expressions in the input code. It can parse a NOT
            expression or a regular boolean expression.

            Returns:
                None
            """
            if next_token.value == "not":
                readToken()
                Bp()
                build_tree("not", 1)
            else:
                Bp()

        # Bp -> A (’gr’ | ’>’ ) A   => ’gr’
        #    -> A (’ge’ | ’>=’) A   => ’ge’
        #    -> A (’ls’ | ’<’ ) A   => ’ls’
        #    -> A (’le’ | ’<=’) A   => ’le’
        #    -> A ’eq’ A            => ’eq’
        #    -> A ’ne’ A            => ’ne’
        #    -> A ;

        def Bp():
            """
            This function is used to parse the boolean expressions in the input code. It can parse a regular
            boolean expression followed by comparison operators.

            Returns:
                None
            """
            A()
            if next_token.value in {"gr", ">"}:
                readToken()
                A()
                build_tree("gr", 2)
            elif next_token.value in {"ge", ">="}:
                readToken()
                A()
                build_tree("ge", 2)
            elif next_token.value in {"ls", "<"}:
                readToken()
                A()
                build_tree("ls", 2)
            elif next_token.value in {"le", "<="}:
                readToken()
                A()
                build_tree("le", 2)
            elif next_token.value == "eq":
                readToken()
                A()
                build_tree("eq", 2)
            elif next_token.value == "ne":
                readToken()
                A()
                build_tree("ne", 2)

        ## Arithmetic Expressions #################################

        # A -> A ’+’ At     => ’+’
        #   -> A ’-’ At     => ’-’
        #   -> ’+’ At
        #   -> ’-’ At       => ’neg’
        #   -> At ;

        def A():
            """
            This function is used to parse the arithmetic expressions in the input code. It can parse an
            arithmetic expression followed by addition or subtraction operators.

            Returns:
                None
            """
            if next_token.value == "+":
                readToken()
                At()
            elif next_token.value == "-":
                readToken()
                At()
                build_tree("neg", 1)
            else:
                At()
                while next_token.value in {"+", "-"}:
                    if next_token.value == "+":
                        readToken()
                        At()
                        build_tree("+", 2)
                    elif next_token.value == "-":
                        readToken()
                        At()
                        build_tree("-", 2)

        # At -> At ’*’ Af    => ’*’
        #    -> At ’/’ Af    => ’/’
        #    -> Af ;

        def At():
            """
            This function is used to parse the arithmetic expressions in the input code. It can parse an
            arithmetic expression followed by multiplication and division operators.

            Returns:
                None
            """
            Af()
            while next_token.value in {"*", "/"}:
                if next_token.value == "*":
                    readToken()
                    Af()
                    build_tree("*", 2)
                elif next_token.value == "/":
                    readToken()
                    Af()
                    build_tree("/", 2)

        # Af -> Ap ’**’ Af      => ’**’
        #    -> Ap ;

        def Af():
            """
            This function is used to parse the arithmetic expressions in the input code. It can parse an
            arithmetic expression followed by exponentiation operator.

            Returns:
                None
            """
            Ap()
            if next_token.value == "**":
                readToken()
                Af()
                build_tree("**", 2)

        # Ap -> Ap ’@’ ’<IDENTIFIER>’ R     => ’@’
        #    -> R ;

        def Ap():
            """
            This function is used to parse the arithmetic expressions in the input code. It can parse an
            arithmetic expression followed by function application.
            
            Returns:
                None
            """
            R()
            while next_token.value == "@":
                readToken()
                if next_token.type == "ID":
                    readToken()
                    R()
                    build_tree("@", 3)
                else:
                    ErrorHandler.handle_error("PARSER : Expected IDENTIFIER ")

        # Rators And Rands #######################################

        # R -> R Rn      => ’gamma’
        #   -> Rn ;

        def R():
            """
            This function is used to parse the arithmetic expressions in the input code. It can parse an
            arithmetic expression followed by function composition.
            
            Returns:
                None
            """
            Rn()
            while next_token.type in {"ID", "INT", "STR"} or next_token.value in {"true", "false", "nil", "(", "dummy"}:
                Rn()
                build_tree("gamma", 2)

        # Rn -> ’<IDENTIFIER>’
        #    -> ’<INTEGER>’
        #    -> ’<STRING>’
        #    -> ’true’              => ’true’
        #    -> ’false’             => ’false’
        #    -> ’nil’               => ’nil’
        #    -> ’(’ E ’)’
        #    -> ’dummy’             => ’dummy’ ;

        def Rn():
            """
            This function is used to parse the atomic arithmetic expressions in the input code. 
            
            Returns:
                None
            """
            if next_token.type in {"ID", "INT", "STR"}:
                readToken()
            elif next_token.value == "true":
                readToken()
                build_tree("<true>", 0)
            elif next_token.value == "false":
                readToken()
                build_tree("<false>", 0)
            elif next_token.value == "nil":
                readToken()
                build_tree("<nil>", 0)
            elif next_token.value == "(":
                readToken()
                E()
                if next_token.value == ")":
                    readToken()
                else:
                    ErrorHandler.handle_error("PARSER : Expected ')' ")
            elif next_token.value == "dummy":
                readToken()
                build_tree("<dummy>", 0)
            else:
                ErrorHandler.handle_error(
                    "PARSER : Expected IDENTIFIER, INTEGER, STRING, true, false, nil, (, dummy ")

        # Definitions ############################################

        # D -> Da ’within’ D        => ’within’
        #   -> Da ;

        def D():
            """
            Parses definitions in the input code.

            Returns:
                None
             """
            Da()
            if next_token.value == "within":
                readToken()
                D()
                build_tree("within", 2)

        # Da -> Dr ( ’and’ Dr )+        => ’and’
        #    -> Dr ;

        def Da():
            """
            Parses definitions in the input code.

             Returns:
                None
             """
            Dr()
            n = 0
            while next_token.value == "and":
                readToken()
                Dr()
                n += 1
            if n > 0:
                build_tree("and", n+1)

        # Dr -> ’rec’ Db    => ’rec’
        #    -> Db ;

        def Dr():
            """
            Parses definitions in the input code.
             
             Returns:
                None
             """
            if next_token.value == "rec":
                readToken()
                Db()
                build_tree("rec", 1)
            else:
                Db()

        # Db -> Vl ’=’ E                    => ’=’
        #    -> ’<IDENTIFIER>’ Vb+ ’=’ E    => ’fcn_form’
        #    -> ’(’ D ’)’ ;

        def Db():
            """
            Parses definitions in the input code.
             
             Returns:
                None
             """
            if next_token.type == "ID":
                if token_list:
                    if token_list[0].value == "=" or token_list[0].value == ",":
                        Vl()
                        readToken()
                        E()
                        build_tree("=", 2)
                    elif token_list[0].type == "ID" or token_list[0].value == "(":
                        readToken()
                        n = 0
                        while True:
                            Vb()
                            n += 1
                            if next_token.type not in {"ID", "("}:
                                break
                        if next_token.value == "=":
                            readToken()
                            E()
                            build_tree("function_form", n+2)
                        else:
                            ErrorHandler.handle_error("PARSER : Expected '=' ")
                else:
                    ErrorHandler.handle_error("PARSER : Expected '=' or 'ID' ")
            elif next_token.value == "(":
                readToken()
                D()
                if next_token.value == ")":
                    readToken()

        # Variables ##############################################

        # Vb -> ’<IDENTIFIER>’
        #    -> ’(’ Vl ’)’
        #    -> ’(’ ’)’             => ’()’;

        def Vb():
            """
            Parses variables in the input code.
             
            Returns:
                None
             """
            if next_token.type == "ID":
                readToken()
            elif next_token.type == "(":
                readToken()
                isV1 = False
                if next_token.type == "ID":
                    Vl()
                    isV1 = True
                if next_token.value == ")":
                    readToken()
                    if isV1 == False:
                        build_tree("<()>", 0)
                else:
                    ErrorHandler.handle_error("PARSER : Expected ')' ")
            else:
                ErrorHandler.handle_error("PARSER : Expected IDENTIFIER, ( ")

        # Vl -> ’<IDENTIFIER>’ list ’,’         => ’,’?

        def Vl():
            """
            Parses comma-separated lists of identifiers in the input code.
             
            Returns:
                None
             """
            n = 0
            while True:
                if next_token.type == "ID":
                    readToken()
                    n += 1
                    if next_token.value == ",":
                        readToken()
                    else:
                        break
                else:
                    ErrorHandler.handle_error("PARSER : Expected IDENTIFIER ")
            if n > 1:
                build_tree(",", n)

        # start of execution
        E()
        if self.stack.size() == 1:
            if not token_list:
                self.status = True
            else:
                ErrorHandler.handle_error(
                    "PARSER : all the tokens are not used ")
        else:
            ErrorHandler.handle_error("PARSER : AST has not created properly ")
