from cse_machine.control_structure import ControlStructure
from utils.control_structure_element import ControlStructureElement


class Linearizer:
    def __init__(self):
        self.control_structures = []
        self.lambda_count = 0
        
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
            self.lambda_count += 1
            self.control_structures[index].push(ControlStructureElement("lambda", "lambda", self.filter(root.children[0].data)[1], self.lambda_count))
            self.preorder_traversal(root.children[1], index+1)

        elif root.data == "tau":
            self.control_structures[index].push(ControlStructureElement("tau", len(root.children)))
            for child in root.children:
                self.preorder_traversal(child, index)

        elif root.data == "->":
            self.control_structures[index].push(ControlStructureElement("delta", "delta",None, index+1))
            self.preorder_traversal(root.children[1], index+1)
            self.control_structures[index].push(ControlStructureElement("delta", "delta",None, index+1))
            self.preorder_traversal(root.children[2], index+2)
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
                    output = ["ID", token[4:-1]]
                elif len(token)>4 and token[1:4] == "INT":
                    output = ["INT", token[5:-1]]
                elif len(token)>4 and token[1:4] == "STR":
                    output = ["STR", token[5:-1]]
                else:
                    output = [token[1:-1], token[1:-1]]
        else:
            output = [token, token]
        return output