from cse_machine.control_structure import ControlStructure
from utils.control_structure_element import ControlStructureElement


class Linearizer:
    def __init__(self):
        self.control_structures = []
        
    def linearize(self,st_tree):

        self.preorder_traversal(st_tree, 0)
        
        return self.control_structures
    
    def preorder_traversal(self, root , index):
        
        if len(self.control_structures) <= index:
            self.control_structures.append(ControlStructure(index))
            
        if not root.children:	
            self.control_structures[index].push(ControlStructureElement(self.filter(root.data)[0], self.filter(root.data)[1]))
            return
        
        if root.data == "lambda":
            
            if root.children[0].data == ",": 
                var_list = []
                for child in root.children[0].children:
                    var_list.append(self.filter(child.data)[1])
                self.control_structures[index].push(ControlStructureElement("lambda", "lambda", var_list, len(self.control_structures)))
            else:
                self.control_structures[index].push(ControlStructureElement("lambda", "lambda", [self.filter(root.children[0].data)[1]], len(self.control_structures)))
            self.preorder_traversal(root.children[1], len(self.control_structures))
            
        elif root.data == "tau":
            self.control_structures[index].push(ControlStructureElement("tau", len(root.children)))
            for child in root.children:
                self.preorder_traversal(child, index)

        elif root.data == "->":
            self.control_structures[index].push(ControlStructureElement("delta", "delta",None, len(self.control_structures)))
            self.preorder_traversal(root.children[1], len(self.control_structures))
            self.control_structures[index].push(ControlStructureElement("delta", "delta",None, len(self.control_structures)))
            self.preorder_traversal(root.children[2], len(self.control_structures))
            self.control_structures[index].push(ControlStructureElement("beta", "beta"))
            self.preorder_traversal(root.children[0], index)
        
        else:
            self.control_structures[index].push(ControlStructureElement(self.filter(root.data)[0], self.filter(root.data)[1]))
                
            self.preorder_traversal(root.children[0], index)
            if len(root.children) > 1:
                self.preorder_traversal(root.children[1], index)
    
    def filter(self,token):
        output = []
        if token[0] == "<":
                if len(token)>3 and token[1:3] == "ID":
                    if token[4:-1] in ["Conc","Print","Stern","Stem","Isstring","Isinteger","Istruthvalue","Isfunction","Null","Istuple","Order","ItoS"]:
                        output = [token[4:-1], token[4:-1]]
                    else:
                        output = ["ID", token[4:-1]]
                elif len(token)>4 and token[1:4] == "INT":
                    output = ["INT", int(token[5:-1])]
                elif len(token)>4 and token[1:4] == "STR":
                    output = ["STR", token[6:-2]]
                elif token[1:-1] == "true":
                    output = ["bool",True]
                elif token[1:-1] == "false":
                    output = ["bool",False]
                elif token[1:-1] == "nil":
                    output = ["nil",None]
                else:
                    output = [token[1:-1], token[1:-1]]
        else:
            output = [token, token]
        return output
    
    def print_control_structures(self):
        print('\n')
        for structure in self.control_structures:
            print(f"δ_{structure.index} = ",end="")
            for element in structure.elements:
                if element.type == "lambda":
                    print(f"λ_{element.control_structure}{element.bounded_variable}",end=" ")
                elif element.type == "delta":
                    print(f"δ_{element.control_structure}",end=" ")
                elif element.type == "tau":
                    print(f"{element.type}[{element.value}]",end=" ")
                elif element.type == "gamma":
                    print("γ",end=" ")
                else:
                    print(element.value,end=" ")
            print("\n")
