from utils.node import Node
from utils.stack import Stack


class Parser:
    def __init__(self):
        self.stack = Stack()

    #   recursive descent parser
    def parse(self, token_list):

        next_token = token_list.pop(0)

        # function to build the tree
        def build_tree(token, n):
            node = Node(token)
            for i in range(n):
                node.add_child(self.stack.pop())
            self.stack.push(node)

        # function to read a token and update to next_token
        def readToken():
            nonlocal next_token
            if token_list:
                next_token = token_list.pop(0)
            if next_token.type in {"ID", "INT", "STR"}:
                build_tree(f"<{next_token.type}:{next_token.value}>", 0)

        # Expressions ############################################

        # E -> ’let’ D ’in’ E   => ’let’
        #   -> ’fn’ Vb+ ’.’ E   => ’lambda’
        #   -> Ew;

        def E():
            if next_token.value == "let":
                readToken()
                D()
                if next_token.value == "in":
                    readToken()
                    E()
                    build_tree("let", 2)
                else:
                    print("Error : Expected 'in' ")

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
                    print("Error : Expected '.' ")
            else:
                Ew()

        # Ew -> T ’where’ Dr    => ’where’
        #    -> T;

        def Ew():
            T()
            if next_token.value == "where":
                readToken()
                Dr()
                build_tree("where", 2)

        ## Tuple Expressions ######################################
        # T -> Ta ( ’,’ Ta )+    => ’tau’
        #   -> Ta ;

        def T():
            Ta()
            if next_token.value == ",":
                n = 0
                while True:
                    readToken()
                    Ta()
                    n += 1
                    if next_token.value != ",":
                        break
                build_tree("tau", n+1)

        # Ta -> Ta ’aug’ Tc      => ’aug’
        #    -> Tc ;

        def Ta():
            if next_token.value == "aug":
                readToken()
                Tc()
                build_tree("aug", 2)
            else:
                Tc()

        # Tc -> B ’->’ Tc ’|’ Tc     => ’->’
        #    -> B ;

        def Tc():
            B()
            if next_token.value == "->":
                readToken()
                Tc()
                if next_token.value == "|":
                    readToken()
                    Tc()
                    build_tree("->", 3)

        ## Boolean Expressions ####################################

        # B -> B ’or’ Bt    => ’or’
        #   -> Bt ;

        def B():
            Bt()
            if next_token.value == "or":
                readToken()
                Bt()
                build_tree("or", 2)

        # Bt -> Bt ’&’ Bs   => ’&’
        #    -> Bs ;

        def Bt():
            Bs()
            if next_token.value == "&":
                readToken()
                Bs()
                build_tree("&", 2)

        # Bs -> ’not’ Bp => ’not’
        #    -> Bp ;

        def Bs():
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
            if next_token.value == "+":
                readToken()
                At()
            elif next_token.value == "-":
                readToken()
                At()
                build_tree("neg", 2)
            else:
                At()
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
            Af()
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
            Ap()
            if next_token.value == "**":
                readToken()
                Af()
                build_tree("**", 2)

        # Ap -> Ap ’@’ ’<IDENTIFIER>’ R     => ’@’
        #    -> R ;

        def Ap():
            R()
            if next_token.value == "@":
                readToken()
                if next_token.type == "ID":
                    readToken()
                    R()
                    build_tree("@", 3)

        # Rators And Rands #######################################

        # R -> R Rn      => ’gamma’
        #   -> Rn ;

        def R():
            n = 0
            while True:
                Rn()
                n += 1
                if next_token.type not in {"ID", "INT", "STR"} and next_token.value not in {"true", "false", "nil", "(", "dummy"}:
                    if n > 1:
                        build_tree("gamma", n)
                    break

        # Rn -> ’<IDENTIFIER>’
        #    -> ’<INTEGER>’
        #    -> ’<STRING>’
        #    -> ’true’              => ’true’
        #    -> ’false’             => ’false’
        #    -> ’nil’               => ’nil’
        #    -> ’(’ E ’)’
        #    -> ’dummy’             => ’dummy’ ;

        def Rn():
            if next_token.type in {"ID", "INT", "STR"}:
                readToken()
            elif next_token.value in {"true", "false", "nil"}:
                build_tree(next_token.value, 0)
                readToken()
            elif next_token.value == "(":
                readToken()
                E()
                if next_token.value == ")":
                    readToken()
                else:
                    print("Error : Expected ')' ")
            elif next_token.value == "dummy":
                readToken()
                build_tree("dummy", 0)
            else:
                print(
                    "Error : Expected IDENTIFIER, INTEGER, STRING, true, false, nil, (, dummy ")

        # Definitions ############################################

        # D -> Da ’within’ D        => ’within’
        #   -> Da ;

        def D():
            Da()
            if next_token.value == "within":
                readToken()
                D()
                build_tree("within", 2)

        # Da -> Dr ( ’and’ Dr )+        => ’and’
        #    -> Dr ;

        def Da():
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
            if next_token.type == "ID":
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
                    build_tree("fcn_form", n+2)
            elif next_token.value == "(":
                readToken()
                D()
                if next_token.value == ")":
                    readToken()
            else:
                Vl()
                if next_token.value == "=":
                    readToken()
                    E()
                    build_tree("=", 2)

        # Variables ##############################################

        # Vb -> ’<IDENTIFIER>’
        #    -> ’(’ Vl ’)’
        #    -> ’(’ ’)’             => ’()’;

        def Vb():
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
                        build_tree("()", 1)
                else:
                    print("Error : Expected ')' ")
            else:
                print("Error : Expected IDENTIFIER, ( ")

        # Vl -> ’<IDENTIFIER>’ list ’,’         => ’,’?

        def Vl():
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
                    print("Error : Expected IDENTIFIER ")
                    break
            if n > 1:
                build_tree(",", n)

        # start of execution
        E()
