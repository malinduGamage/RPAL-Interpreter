#cse_machine/machine.py


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
        self._error_handler = CseErrorHandler(self)
        self.control_structures = None
        self.environment_tree = Environment()
        self.current_env = self.environment_tree
        self.stack = Stack()
        self.control = Stack()
        self._linearizer = Linearizer()
        self._outputs = []
        self.table_data = []
        self.binary_operator = {"+", "-", "/", "*", "**", "eq", "ne", "gr", "ge", "le",">", "<", ">=", "<=", "or", "&", "aug", "ls", "Conc"}
        self.unary_operators =  {
            "Print", "Isstring", "Isinteger", "Istruthvalue", "Isfunction", "Null",
            "Istuple", "Order", "Stern", "Stem", "ItoS", "neg", "not", "$ConcPartial"
            }

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
        
        
        self.control_structures = self._linearizer.linearize(st_tree)
        self._linearizer.print_control_structures()
        
        self.initialize()
        
        while not self.control.is_empty():
            control_top = self.control.peek()
            stack_top = self.stack.peek()
            #self._print_cse_table()
            if control_top.type in ['ID','STR','INT','bool','tuple','Y*','nil','dummy']:
                self.CSErule1()
            elif control_top.type == "lambda":
                self.CSErule2()
                #print("out of rule 2")
            elif control_top.type == "env_marker":
                self.CSErule5()
                #print("out of rule 5")
            elif control_top.value in self.binary_operator and self.stack.size() >= 2:
                self.CSErule6()
                #print("out of rule 6")
            elif control_top.value in self.unary_operators and self.stack.size() >= 1:
                self.CSErule7()
                #print("out of rule 7")
            elif control_top.type == "beta" and self.stack.size() >= 1:
                self.CSErule8()
                #print("out of rule 8")
            elif control_top.type == "tau":
                self.CSErule9()
                #print("out of rule 9")
            elif control_top.type == "gamma" and stack_top.type == "tuple":
                self.CSErule10()
                #print("out of rule 10")
            elif control_top.type == "gamma" and stack_top.type == "Y*":
                self.CSErule12()
                #print("out of rule 12")
            elif control_top.type == "gamma" and stack_top.type == "eta":
                self.CSErule13()
                #print("out of rule 13") 
            elif control_top.type == "gamma"  and stack_top.type == "lambda":
                    if len(stack_top.bounded_variable) > 1:
                        self.CSErule11()
                        #print("out of rule 11")
                    else:
                        self.CSErule4()
                        #print("out of rule 4")
            else:
                self._error_handler.handle_error("CSE : Invalid control structure")

    def CSErule1(self):
        #print("rule 1")
        self._add_table_data("1")
        control_top = self.control.peek()
        if control_top.type in ['STR','INT','bool','tuple','Y*','nil','dummy']:
            self.stack.push(self.control.pop())
        else :
            item = self.control.pop()
            var_name = item.value
            #print("hey")
            var = self._var_lookup(var_name)
            if var[0] == "eta" or var[0] == "lambda":
                self.stack.push(var[1])
            else :
                self.stack.push(ControlStructureElement(var[0],var[1]))
        #print("out of rule 1")
        
    def CSErule2(self):
        #print("rule 2")
        self._add_table_data("2")
        lambda_ = self.control.pop()
        lambda_.env = self.current_env
        self.stack.push(lambda_)
        
    def CSErule3(self):
        #print("rule 3")
        self._add_table_data("3")
        pass
    
    def CSErule4(self):
        #print("rule 4")
        self._add_table_data("4")
        if self.current_env.index >= 1000:
            self._error_handler.handle_error("CSE : Environment limit exceeded")
        self.control.pop()
        lambda_ = self.stack.pop()
        rand = self.stack.pop()
        #print("rand=",rand,"lambda=",lambda_.bounded_variable[0])
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
        #print("rule 5")
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
        #print("rule 6")
        self._add_table_data("6")
        binop = self.control.pop().value
        rator = self.stack.pop()
        rand = self.stack.pop()
        if binop == "aug":
            self.stack.push(self._apply_binary(rator,rand,binop))
        elif binop == "Conc":
            if rator.type == "STR" and rand.type == "STR":
                result =self._apply_binary(rator.value,rand.value,binop)
                #print("rator=",rator.value,"rand=",rand.value,"result=",result)
                self.stack.push(ControlStructureElement("STR",result))
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
            #print("rator=",rator,"rand=",rand,"result=",result)
            self.stack.push(ControlStructureElement(typ,result))
        
        
    def CSErule7(self):
        #print("rule 7")
        self._add_table_data("7")
        unop = self.control.pop().value
        rator_e = self.stack.pop()
        #print(unop,rator_e.type)
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
        #print("rator=",rator_e.value,"unop",unop,"result=",result)
        self.stack.push(ControlStructureElement(res_type,result))
                    
    def CSErule8(self):
        #print("rule 8")
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
        #print("rule 9")
        self._add_table_data("9")
        tau = self.control.pop()
        n = tau.value
        tup = []
        for i in range(n):
            tup.append(self.stack.pop())
        self.stack.push(ControlStructureElement("tuple",tup))
                
    def CSErule10(self):
        #print("rule 10")
        self._add_table_data("10")
        self.control.pop()
        l = self.stack.pop()
        index = self.stack.pop()
        if index.type != "INT":
            self._error_handler.handle_error("CSE : Invalid index")
        index  = index.value-1
        self.stack.push(l.value[index])
                
    def CSErule11(self):
        #print("rule 11")
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
        #print("rule 12")
        self._add_table_data("12")
        self.control.pop()
        self.stack.pop()
        lambda_ = self.stack.pop()
        if lambda_.type != "lambda":
            self._error_handler.handle_error("CSE : expected lambda")
        eta = ControlStructureElement("eta","eta",lambda_.bounded_variable,lambda_.control_structure,lambda_.env)
        self.stack.push(eta)
        
    def CSErule13(self):
        #print("rule 13")
        self._add_table_data("13")
        self.control.push(ControlStructureElement("gamma","gamma"))
        eta = self.stack.peek()
        self.stack.push(ControlStructureElement("lambda","lambda",eta.bounded_variable,eta.control_structure,eta.env))
                
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

    def _generate_output(self):
        return "".join(self._outputs)+"\n"
    
    def _generate_raw_output(self):
        return raw(self._generate_output()) 