# cse_machine/machine.py

"""
Control Structure Environment (CSE) Machine for Executing RPAL Programs.

Description:
This file contains the implementation of the Control Structure Environment (CSE) machine, which is responsible for executing RPAL programs by interpreting the Standardized Tree (ST) generated by the parser. It contains the CSEMachine class with methods for executing the ST and applying the necessary control structure rules.

Usage:
The CSEMachine class is used to interpret RPAL programs by executing the Standardized Tree (ST) representation generated during the parsing phase. It provides methods to execute the ST and apply control structure rules to evaluate expressions and perform operations defined in the RPAL language.

Example Usage:
1. Create an instance of the CSEMachine class:
   cse_machine = CSEMachine()

2. Initialize the machine with the control structures and environment:
   cse_machine.initialize()

3. Execute the RPAL program by passing the Standardized Tree (ST):
   st_tree = generate_standardized_tree(rpal_program)
   cse_machine.execute(st_tree)

4. Retrieve the output of the program:
   output = cse_machine.get_output()
   print("Output:", output)
"""


from errors_handling.cse_error_handler import CseErrorHandler
from cse_machine.data_structures.control_structure import ControlStructure
from cse_machine.data_structures.enviroment import Environment
from cse_machine.data_structures.stack import Stack
from cse_machine.utils.STlinearizer import Linearizer
from cse_machine.utils.util import add_table_data, print_cse_table , var_lookup , raw
from cse_machine.apply_operations.apply_bin import apply_binary
from cse_machine.apply_operations.apply_un import apply_unary
from utils.node import Node	
from utils.control_structure_element import ControlStructureElement


class CSEMachine:
    """
    Control Structure Environment (CSE) Machine for executing RPAL programs.

    Attributes:
        _error_handler (CseErrorHandler): Error handler instance for managing errors during execution.
        control_structures (list): List of control structures extracted from the Standardized Tree (ST).
        environment_tree (Environment): Environment tree representing the current execution environment.
        current_env (Environment): Reference to the current environment in the environment tree.
        stack (Stack): Stack for managing the execution stack.
        control (Stack): Stack for managing the control structures during execution.
        _linearizer (Linearizer): Linearizer instance for converting the ST to linear form.
        binary_operator (set): Set of binary operators supported by the RPAL language.
        unary_operators (set): Set of unary operators supported by the RPAL language.
        _outputs (list): List to store the output generated during execution.
        table_data (list): List to store data for generating the execution table.
    """

    def __init__(self):
        """
        Initialize the CSEMachine with necessary components.
        """
        # Initialize the error handler
        self._error_handler = CseErrorHandler(self)

        # Initialize the linearizer for converting the ST to linear form
        self._linearizer = Linearizer()

        # Initialize the control structures, environment, and stacks
        self.control_structures = None
        self.environment_tree = Environment()
        self.current_env = self.environment_tree
        self.stack = Stack()
        self.control = Stack()
        
        # Initialize the output and table data
        self._outputs = list()
        self.table_data = list()

        # binary operators supported by RPAL and inbuilt functions(Conc)

        self.binary_operator = {
                                # Arithmetic operators
                                "+", "-", "/", "*", "**", 
                                # Operators for comparison and logical operations
                                "eq", "ne", "gr", "ge", "le","ls",
                                # Relational operators 
                                ">", "<", ">=", "<=", 
                                # Logical operators 
                                "or", "&", "aug",  
                                # Operators for string concatenation (RPAL inbuilt function)
                                "Conc"
                                }
        
        # unary operators supported by RPAL and inbuilt functions

        self.unary_operators =  {
                                # Unary operators
                                "neg", "not",
                                # print inbuilt functions
                                "Print", 
                                # type checking inbuilt functions
                                "Isstring", "Isinteger", "Istruthvalue", "Isfunction", "Null","Istuple",
                                # String manipulation inbuilt functions
                                "Order", "Stern", "Stem", "ItoS", "$ConcPartial"
                                }

    def initialize(self):
        """
        Initialize the CSEMachine with necessary components.

         :return: None
        """
        # Push an environment marker onto the stack and control structures
        env_marker = ControlStructureElement("env_marker", "env_marker", None, None, self.current_env)
        self.stack.push(env_marker)
        self.control.push(env_marker)

        # Push elements from the first control structure onto the control stack
        if self.control_structures:
            elements = self.control_structures[0].elements
            for element in elements:
                self.control.push(element)
        else:
            # Handle the case when control_structures is empty
            self._error_handler.handle_error("Control structures are empty")

    def execute(self, st_tree):
        """
        Execute the given Standardized Tree (ST).

        Args:
            st_tree (Node): The root node of the Standardized Tree (ST) to execute.
        """
        
        # Get the linearized control structures from the ST
        self.control_structures = self._linearizer.linearize(st_tree)
        
        # Initialize the CSE machine
        self.initialize()
        
        # Execute the ST
        while not self.control.is_empty():

            # get the top of the control stack
            control_top = self.control.peek()
            # get the top of the stack
            stack_top = self.stack.peek()

            # check the type of the control structure and apply the corresponding rule

            if control_top.type in ['ID','STR','INT','bool','tuple','Y*','nil','dummy']:
                self.CSErule1()
            elif control_top.type == "lambda":
                self.CSErule2()
            elif control_top.type == "env_marker":
                self.CSErule5()
            elif control_top.value in self.binary_operator and self.stack.size() >= 2:
                self.CSErule6()
            elif control_top.value in self.unary_operators and self.stack.size() >= 1:
                self.CSErule7()
            elif control_top.type == "beta" and self.stack.size() >= 1:
                self.CSErule8()
            elif control_top.type == "tau":
                self.CSErule9()
            elif control_top.type == "gamma" and stack_top.type == "tuple":
                self.CSErule10()
            elif control_top.type == "gamma" and stack_top.type == "Y*":
                self.CSErule12()
            elif control_top.type == "gamma" and stack_top.type == "eta":
                self.CSErule13()
            elif control_top.type == "gamma"  and stack_top.type == "lambda":
                    if len(stack_top.bounded_variable) > 1:
                        self.CSErule11()
                    else:
                        self.CSErule4()
            elif control_top.type == "gamma" and stack_top.type == "ConcPartial":
                self.Concpartial()
            else:
                self._error_handler.handle_error("CSE : Invalid control structure")

    def CSErule1(self):
        """
        CSE rule 1: If the top of the control stack is a variable, constant, or tuple,
        push it onto the stack. If the top of the control stack is a control structure,
        check whether it is a variable or a lambda expression. If it is a variable,
        look up its value in the environment and push it onto the stack. If it is a
        lambda expression, push it onto the stack.
        """
        self._add_table_data("1")
        control_top = self.control.peek()
        if control_top.type in ['STR','INT','bool','tuple','Y*','nil','dummy']:
            self.stack.push(self.control.pop())
        else :
            item = self.control.pop()
            var_name = item.value
            var = self._var_lookup(var_name)
            if var[0] == "eta" or var[0] == "lambda":
                self.stack.push(var[1])
            else :
                self.stack.push(ControlStructureElement(var[0],var[1]))
        
    def CSErule2(self):
        """
        CSE rule 2: If the top of the control stack is a lambda expression,
        push it onto the stack. Set the environment of the lambda expression to the current environment.
        """
        self._add_table_data("2")
        lambda_ = self.control.pop()
        lambda_.env = self.current_env
        self.stack.push(lambda_)
        
    def CSErule3(self):
        self._add_table_data("3")
        pass
    
    def CSErule4(self):
        """
        CSE rule 4: If the top of the control stack is a lambda expression,
        push it onto the stack. Set the environment of the lambda expression to the current environment.
        """
        self._add_table_data("4")
        if self.current_env.index >= 2000:
            self._error_handler.handle_error("CSE : Environment limit exceeded")
        self.control.pop()
        lambda_ = self.stack.pop()
        rand = self.stack.pop()
        new_env = Environment()
        if rand.type  == "eta" or rand.type == "lambda":
            new_env.add_var(lambda_.bounded_variable[0],rand.type,rand)
        elif rand.type in ["tuple","INT","bool","STR","nil"]:
            new_env.add_var(lambda_.bounded_variable[0],rand.type,rand.value)
        else:
            self._error_handler.handle_error("CSE : Invalid type")
        new_env.parent = lambda_.env

        self.current_env = new_env
        
        env_marker = ControlStructureElement("env_marker","env_marker",None,None,new_env)
        
        self.control.push(env_marker)
        
        for element in self.control_structures[lambda_.control_structure].elements:
            self.control.push(element)
            
        self.stack.push(env_marker)
        
    def CSErule5(self):
        """
        CSE rule 5: If the top of the control stack is an environment marker,
        pop it off the stack and set the current environment to the environment
        it represents. Then, pop the value off the stack and push it back on.
        Finally, iterate over the entire stack, starting from the bottom, and
        check if the current element is an environment marker. If it is, set the
        current environment to the environment it represents and break out of the loop.
        If the environments do not match, raise an error.

        Parameters:
            None

        Returns:
            None

        Raises:
            CseError: If the environments do not match
        """
        self._add_table_data("5")
        env = self.control.pop().env
        value = self.stack.pop()
        if env == self.stack.pop().env:
            self.stack.push(value)
            for element in reversed(self.stack.whole_stack()):
                if element.type == "env_marker":
                    self.current_env = element.env
                    break
        else:
            self._error_handler.handle_error("CSE : Invalid environment")
                
    def CSErule6(self):
        """
        CSE rule 6: If the top of the control stack is a binary operation,
        pop two elements from the stack, apply the binary operation to the
        two popped elements, and push the result back onto the stack.
        If the top of the control stack is "aug", pop two elements from the stack,
        apply the addition operator to the two popped elements, and push the result back onto the stack.
        If the top of the control stack is "Conc", pop two elements from the stack,
        check if both elements are of type "STR", and if so, concatenate the two strings and push the result back onto the stack.
        If one of the two elements is not of type "STR", replace the element with type "ConcPartial" and push the other element back onto the stack.
        If both elements are not of type "STR", raise an error.
        """
        self._add_table_data("6")
        binop = self.control.pop().value
        rator = self.stack.pop()
        rand = self.stack.pop()
        if binop == "aug":
            self.stack.push(self._apply_binary(rator,rand,binop))
        elif binop == "Conc":
            if rator.type == "STR" and rand.type == "STR":
                result =self._apply_binary(rator.value,rand.value,binop)
                self.stack.push(ControlStructureElement("STR",result))
                while self.control.peek().type == "gamma":
                    self.control.pop()
            elif rator.type == "STR":
                rator.type = "ConcPartial"
                self.stack.push(rand)
                self.stack.push(rator)
                while self.control.peek().type == "gamma":
                    self.control.pop()
            else:
                self._error_handler.handle_error("CSE : Invalid type for concatenation")
        else:
            rator = rator.value
            rand = rand.value
            result = self._apply_binary(rator,rand,binop)
            typ  = None
            if type(result) == bool:
                typ = "bool"
            else:
                typ = "INT"
            self.stack.push(ControlStructureElement(typ,result))
        
        
    def CSErule7(self):
        """
        CSE rule 7: If the top of the control stack is a unary operation,
        pop one element from the stack, apply the unary operation to the
        popped element, and push the result back onto the stack.
        If the top of the control stack is "neg", pop one element from the stack,
        apply the negation operator to the popped element, and push the result back onto the stack.
        If the top of the control stack is "not", pop one element from the stack,
        """

        self._add_table_data("7")
        unop = self.control.pop().value
        rator_e = self.stack.pop()
        result = self._apply_unary(rator_e,unop)
        res_type = None
        if type(result) == bool:
            res_type = "bool"
        elif type(result) == str:
            res_type = "STR"
        else :
            res_type = "INT"
        while self.control.peek().type == "gamma":
            self.control.pop()
        self.stack.push(ControlStructureElement(res_type,result))
                    
    def CSErule8(self):
        """
        CSE rule 8: If the top of the control stack is a boolean value,
        pop it off the stack and check if it is True or False. If it is True,
        pop two elements from the stack, check if the second element is a control structure,
        and if so, replace the second element with the elements from the control structure.
        Then, pop the first element off the stack and push it back on.
        If the second element is not a control structure, raise an error.
        If the boolean value is False, pop two elements from the stack,
        check if the first element is a control structure, and if so, replace the first element
        with the elements from the control structure. Then, pop the second element off the stack
        and push it back on. If the first element is not a control structure, raise an error.
        """
        self._add_table_data("8")
        val = self.stack.pop().value
        if val == True :
            self.control.pop()
            self.control.pop()
            delta = self.control.pop()
            for element in self.control_structures[delta.control_structure].elements:
                self.control.push(element)
        elif val == False:
            self.control.pop()
            delta = self.control.pop()
            self.control.pop()
            for element in self.control_structures[delta.control_structure].elements:
                self.control.push(element)
        else:
            self._error_handler.handle_error("CSE : Invalid type for condition")

    def CSErule9(self):
        """
        CSE rule 9: If the top of the control stack is a "tau" node,
        pop it off the stack and create a new tuple with the next "n" elements
        on the stack. Push the tuple back onto the stack.
        """
        self._add_table_data("9")
        tau = self.control.pop()
        n = tau.value
        tup = []
        for i in range(n):
            tup.append(self.stack.pop())
        self.stack.push(ControlStructureElement("tuple",tup))
                
    def CSErule10(self):
        """
        CSE rule 10: If the top of the control stack is a tuple, pop it off the stack,
        retrieve the index from the stack, and retrieve the element at the given index from the tuple.
        If the index is out of bounds, raise an error. Push the retrieved element back onto the stack.
        """
        self._add_table_data("10")
        self.control.pop()
        l = self.stack.pop()
        index = self.stack.pop()
        if index.type != "INT":
            self._error_handler.handle_error("CSE : Invalid index")
        index  = index.value-1
        self.stack.push(l.value[index])
                
    def CSErule11(self):
        """
        CSE rule 11: If the top of the control stack is a lambda expression,
        pop it off the stack and retrieve the bounded variables, control structure, and environment from the lambda expression.
        Create a new environment with the same parent as the environment of the lambda expression.
        Pop the next "n" elements from the stack, where "n" is the number of arguments of the lambda expression.
        For each element popped from the stack, add it to the new environment with the same type as the element.
        Set the current environment to the new environment.
        Push an environment marker onto the stack with the new environment as its environment.
        Push the elements from the control structure associated with the lambda expression onto the control stack.
        """
        self._add_table_data("11")
        self.control.pop()
        lambda_ = self.stack.pop()
        var_list = lambda_.bounded_variable
        k = lambda_.control_structure
        c = lambda_.env
        
        new_env = Environment()
        rand = self.stack.pop()
        
        if len(var_list) != len(rand.value):
            self._error_handler.handle_error("CSE : Invalid number of arguments")
            
        for i in range(len(var_list)):
            if rand.value[i].type == "eta" or rand.value[i].type == "lambda":
                new_env.add_var(var_list[i],rand.value[i].type,rand.value[i])
            else:
                new_env.add_var(var_list[i],rand.value[i].type,rand.value[i].value)
        
        new_env.parent = c
        self.current_env = new_env
        env_marker = ControlStructureElement("env_marker","env_marker",None,None,new_env)
        self.stack.push(env_marker)
        self.control.push(env_marker)
        
        for element in self.control_structures[k].elements:
            self.control.push(element)
            
    def CSErule12(self):
        """
        CSE rule 12: If the top of the control stack is a "tau" node,
        pop it off the stack and create a new tuple with the next "n" elements
        on the stack. Push the tuple back onto the stack.
        """
        self._add_table_data("12")
        self.control.pop()
        self.stack.pop()
        lambda_ = self.stack.pop()
        if lambda_.type != "lambda":
            self._error_handler.handle_error("CSE : expected lambda")
        eta = ControlStructureElement("eta","eta",lambda_.bounded_variable,lambda_.control_structure,lambda_.env)
        self.stack.push(eta)
        
    def CSErule13(self):
        """
        CSE rule 13: If the top of the control stack is a "tau" node,
        pop it off the stack and create a new tuple with the next "n" elements
        on the stack. Push the tuple back onto the stack.
        """
        self._add_table_data("13")
        self.control.push(ControlStructureElement("gamma","gamma"))
        eta = self.stack.peek()
        self.stack.push(ControlStructureElement("lambda","lambda",eta.bounded_variable,eta.control_structure,eta.env))
    
    def Concpartial(self):
        rator = self.stack.pop()
        rand = self.stack.pop()
        if rand.type == "STR":
            result = self._apply_binary(rator.value,rand.value,"Conc")
            self.stack.push(ControlStructureElement("STR",result))
            while self.control.peek().type == "gamma":
                    self.control.pop()
        else:
            self._error_handler.handle_error("CSE : Invalid type for concatenation")
            
    
    def _var_lookup(self , var_name):
        return var_lookup(self, var_name)
            
    def _apply_binary(self , rator , rand , binop):
        return apply_binary(self, rator, rand, binop)
                
    def _apply_unary(self , rator , unop):
        return apply_unary(self, rator, unop)     

    def _add_table_data(self, rule):
        add_table_data(self, rule)

    def _print_cse_table(self):
        self._linearizer.print_control_structures()
        print_cse_table(self)

    def _generate_output(self):
        return "".join(self._outputs)+"\n"
    
    def _generate_raw_output(self):
        return raw(self._generate_output()) 