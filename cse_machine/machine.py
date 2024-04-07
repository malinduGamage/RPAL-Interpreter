from errors_handling.error_handler import ErrorHandler
from cse_machine.control_structure import ControlStructure
from cse_machine.enviroment import Environment
from cse_machine.stack import Stack
from cse_machine.STlinearizer import Linearizer
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

    def execute(self, st_tree):
        """
        Execute the given Standardized Tree (ST).

        Args:
            st_tree (Node): The root node of the Standardized Tree (ST) to execute.
        """
        binary_operators = ["aug","or","&","+","-","/","**","*","gr","ge","ls","le","eq","ne"]
        unary_operators = ["not", "neg"]
        
        self.control_structures = self._linearizer.linearize(st_tree)
        self._linearizer.print_control_structures()
        
        self.initialize()
        while not self.control.is_empty():
            
            control_top = self.control.peek()
            stack_top = self.stack.peek()   
            
            print("\nstack\n----------------------")
            for element in self.stack.whole_stack():
                print(element.value)
            print("----------------------")
            print("\ncontrol\n----------------------")
            for element in self.control.whole_stack():
                print(element.value)
            print("----------------------")
            
            if control_top.type == "ID":
                self.CSErule1()
            elif control_top.type == "lambda":
                self.CSErule2()
            elif control_top.type == "gamma" and stack_top.type == "lambda":
                if len(stack_top.bounded_variable) > 1:
                    self.CSErule11()
                else:
                    self.CSErule4()
            elif control_top.type == "env_marker":##################
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
            elif control_top.type in ['ID','STR','INT','bool','tuple']:
                self.stack.push(self.control.pop())
            else:
                print("\nstack\n---------------------")
                for element in self.stack.whole_stack():
                    print(element.value)
                
                print("----------------------------\ncontrol\n---------------------------")
                for element in self.control.whole_stack():
                    print(element.value)
                print("----------------------------")
                self._error_handler.handle_error("CSE : Invalid control structure")
                
                
        print("\nstack\n----------------------")
        for element in self.stack.whole_stack():
            print(element.value)
        print("----------------------")
        print("\ncontrol\n----------------------")
        for element in self.control.whole_stack():
            print(element.value)
        print("----------------------")
        
    def var_lookup(self , var_name):
        env_pointer = self.current_env
        while env_pointer.parent != None:
            if var_name in env_pointer._environment:
                
                print(var_name,env_pointer._environment[var_name],"==========================")
                return env_pointer._environment[var_name]
            env_pointer = env_pointer.parent
        else:
            self._error_handler.handle_error("CSE : Variable not found in the environment")
            
    def apply_binary(self , rator , rand , binop):
        
        
        if binop == "aug":
            if rator== "nil":
                if rand == "nil":
                    return None
                return rand
            elif rand == "nil":
                return rator
            elif type(rator) == list:
                rator.append(rand)
                return rator
            else:
                return [rator , rand]
            
        elif binop == "or":
            if type(rator) == bool and type(rand) == bool:
                return rator or rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
        
        elif binop == "&":
            if type(rator) == bool and type(rand) == bool:
                return rator and rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
        elif binop == "+":
            if type(rator) == int and type(rand) == int:
                return rator + rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
        elif binop == "-":
            if type(rator) == int and type(rand) == int:
                return rator - rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
        elif binop == "*":
            if type(rator) == int and type(rand) == int:
                return rator * rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
        elif binop == "/":
            if type(rator) == int and type(rand) == int:
                return rator // rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
        elif binop == "**":
            if type(rator) == int and type(rand) == int:
                return rator ** rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
        elif binop == "gr":
            if type(rator) == int and type(rand) == int:
                return rator > rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
        elif binop == "ge":
            if type(rator) == int and type(rand) == int:
                return rator >= rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
        elif binop == "ls":
            if type(rator) == int and type(rand) == int:
                return rator < rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
        elif binop == "le":
            if type(rator) == int and type(rand) == int:
                return rator <= rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
        elif binop == "eq":
            if type(rator) == int and type(rand) == int:
                return rator == rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
        elif binop == "ne":
            if type(rator) == int and type(rand) == int:
                return rator != rand
            else:
                self._error_handler.handle_error("CSE : Invalid binary operation")
                
    def apply_unary(self , rator , unop):
        
        if unop == "not":
            if type(rator) == bool :
                return not rator
            else:
                self._error_handler.handle_error("CSE : Invalid unary operation")
                
        elif unop == "neg":
            if type(rator) == int:
                return -rator
            else:
                self._error_handler.handle_error("CSE : Invalid unary operation")
        
    def initialize(self):
        self.stack.push(ControlStructureElement("env_marker","env_marker",None,None,self.current_env))
        self.control.push(ControlStructureElement("env_marker","env_marker",None,None,self.current_env))
        for element in self.control_structures[0].elements:
            self.control.push(element)
        
    def CSErule1(self):
        print("rule 1")
        var_name = self.control.pop().value
        var = self.var_lookup(var_name)
        var_type = var[0]
        var_val = var[1]
        self.stack.push(ControlStructureElement(var_type,var_val))
        
    def CSErule2(self):
        print("rule 2")
        lambda_ = self.control.pop()
        lambda_.env = self.current_env
        self.stack.push(lambda_)
        
    def CSErule4(self):
        print("rule 4")
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
        print("rule 5")
        self.control.pop()
        value = self.stack.pop()
        self.stack.pop()
        self.stack.push(value)
        
    def CSErule6(self):
        print("rule 6")
        binop = self.control.pop().value
        rator = self.stack.pop().value
        rand = self.stack.pop().value
        result = self.apply_binary(rator,rand,binop)
        self.stack.push(ControlStructureElement("bool",result))
        
    def CSErule7(self):
        print("rule 7")
        unop = self.control.pop().value
        rator = self.stack.pop().value
        result = self.apply_unary(rator,unop)
        if type(result) == bool:
            self.stack.push(ControlStructureElement("bool",result))
        else:
            self.stack.push(ControlStructureElement("INT",result))
            
    def CSErule8(self):
        print("rule 8")
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
        print("rule 9")
        tau = self.control.pop()
        n = tau.value
        l = []
        for i in range(n):
            l.append(self.stack.pop())
        self.stack.push(ControlStructureElement("tuple",l))
        
    def CSErule10(self):
        print("rule 10")
        self.control.pop()
        l = self.stack.pop()
        index = self.stack.pop()

        self.stack.push(ControlStructureElement(l[index].type,l[index]))
        
    def CSErule11(self):
        print("rule 11")
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
        