from errors_handling.error_handler import ErrorHandler
from cse_machine.control_structure import ControlStructure
from cse_machine.enviroment import Environment
from cse_machine.stack import Stack
from cse_machine.STlinearizer import Linearizer
from cse_machine.util import add_table_data, print_cse_table , var_lookup
from cse_machine.apply_bin import apply_binary
from cse_machine.apply_un import apply_unary
from utils.node import Node	
from utils.control_structure_element import ControlStructureElement


class CSEMachine:
    """
    Class representing the Control Structure Environment (CSE) machine for executing RPAL programs.

    Attributes:
        _error_handler (ErrorHandler): Error handler instance for managing errors during execution.
        _linearizer (Linearizer): Linearizer instance for converting the Standardized Tree (ST) to linear form.
        _control_structure (ControlStructure): ControlStructure instance for managing control flow.
        _current_environment (Environment): Environment instance representing the current execution environment.
        _stack (Stack): Stack instance for managing the execution stack.
    """

    def __init__(self):
        """
        Initialize the CSEMachine with necessary components.
        """
        self._error_handler = ErrorHandler()
        self.control_structures = None
        self.environment_tree = Environment()
        self.current_env = self.environment_tree
        self.stack = Stack()
        self.control = Stack()
        self._linearizer = Linearizer()
        self.table_data = []

    def initialize(self):
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
        binary_operators = {"+", "-", "/", "*", "**", "eq", "ne", "gr", "ge", "le",">", "<", ">=", "<=", "or", "&", "aug", "ls"}
        unary_operators =  {
            "Print", "Isstring", "Isinteger", "Istruthvalue", "Isfunction", "Null",
            "Istuple", "Order", "Stern", "Stem", "ItoS", "neg", "not", "$ConcPartial"
            }
        
        self.control_structures = self._linearizer.linearize(st_tree)
        self._linearizer.print_control_structures()
        
        self.initialize()

        while not self.control.is_empty():
            control_top = self.control.peek()
            stack_top = self.stack.peek()

            if control_top.type in ['ID','STR','INT','bool','tuple']:
                self.CSErule1()
            elif control_top.type == "lambda":
                self.CSErule2()
            elif control_top.type == "gamma" and stack_top.type == "lambda":
                if len(stack_top.bounded_variable) > 1:
                    self.CSErule11()
                else:
                    self.CSErule4()
            elif control_top.type == "env_marker":
                self.CSErule5()
            elif control_top.value in binary_operators and self.stack.size() >= 2:
                self.CSErule6()
            elif control_top.value in unary_operators and self.stack.size() >= 1:
                self.CSErule7()
            elif control_top.type == "beta" and self.stack.size() >= 1:
                self.CSErule8()
            elif control_top.type == "tau":
                self.CSErule9()
            elif control_top.type == "gamma" and stack_top.type == "tuple":
                self.CSErule10()
            else:
                pass

        
    def CSErule1(self):
        self._add_table_data("1")
        control_top = self.control.peek()
        if control_top.type in ['STR','INT','bool','tuple']:
            self.stack.push(self.control.pop())
        else :
            var_name = self.control.pop().value
            var = self._var_lookup(var_name)
            var_type = var[0]
            var_val = var[1]
            self.stack.push(ControlStructureElement(var_type,var_val))
        
    def CSErule2(self):
        self._add_table_data("2")
        lambda_ = self.control.pop()
        lambda_.env = self.current_env
        self.stack.push(lambda_)
        
    def CSErule3(self):
        pass
    def CSErule4(self):
        self._add_table_data("4")
        self.control.pop()
        lambda_ = self.stack.pop()
        rand = self.stack.pop()
        new_env = Environment()
        new_env.add_var(lambda_.bounded_variable[0],rand.type,rand.value)
        new_env.parent = lambda_.env
        lambda_.env.add_child(new_env)
        
        self.current_env = new_env
        
        env_marker = ControlStructureElement("env_marker","env_marker",None,None,new_env)
        
        self.control.push(env_marker)
        
        for element in self.control_structures[lambda_.control_structure].elements:
            self.control.push(element)
            
        self.stack.push(env_marker)
        
    def CSErule5(self):
        self._add_table_data("5")
        self.control.pop()
        value = self.stack.pop()
        self.stack.pop()
        self.stack.push(value)
        
        for element in reversed(self.stack.whole_stack()):
            if element.type == "env_marker":
                self.current_env = element.env
                break
                
    def CSErule6(self):
        self._add_table_data("6")
        binop = self.control.pop().value
        rator = self.stack.pop().value
        rand = self.stack.pop().value
        result = self._apply_binary(rator,rand,binop)
        self.stack.push(ControlStructureElement("bool",result))
        
    def CSErule7(self):
        self._add_table_data("7")
        unop = self.control.pop().value
        rator = self.stack.pop().value
        result = self._apply_unary(rator,unop)
        if type(result) == bool:
            self.stack.push(ControlStructureElement("bool",result))
        else:
            self.stack.push(ControlStructureElement("INT",result))
                    
    def CSErule8(self):
        self._add_table_data("8")
        if self.stack.pop().value == True :
            self.control.pop()
            self.control.pop()
            delta = self.control.pop()
            for element in self.control_structures[delta.control_structure].elements:
                self.control.push(element)
        else :
            self.control.pop()
            delta = self.control.pop()
            self.control.pop()
            for element in self.control_structures[delta.control_structure].elements:
                self.control.push(element)
                   
    def CSErule9(self):
        self._add_table_data("9")
        tau = self.control.pop()
        n = tau.value
        l = []
        for i in range(n):
            l.append(self.stack.pop())
        self.stack.push(ControlStructureElement("tuple",l))
                
    def CSErule10(self):
        self._add_table_data("10")
        self.control.pop()
        l = self.stack.pop()
        index = self.stack.pop()

        self.stack.push(ControlStructureElement(l[index].type,l[index]))
                
    def CSErule11(self):
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
            new_env.add_var(var_list[i],rand.value[i].type,rand.value[i].value)
        
        new_env.parent = c
        c.add_child(new_env)
        self.current_env = new_env
        env_marker = ControlStructureElement("env_marker","env_marker",None,None,new_env)
        self.stack.push(env_marker)
        self.control.push(env_marker)
        
        for element in self.control_structures[k].elements:
            self.control.push(element)
        
    def _var_lookup(self , var_name):
        return var_lookup(self, var_name)
            
    def _apply_binary(self , rator , rand , binop):
        return apply_binary(self, rator, rand, binop)
                
    def _apply_unary(self , rator , unop):
        return apply_unary(self, rator, unop)     

    def _add_table_data(self, rule):
        add_table_data(self, rule)

    def _print_cse_table(self):
        print_cse_table(self)


        