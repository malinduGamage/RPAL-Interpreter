class Environment:
    index = -1
    def __init__(self , parent = None):
        self.index = Environment.index +1
        self._environment = {} #name:[type, value]
        self.children = []
        self.parent = parent
        
    def add_var(self, name, type, value):
        self._environment[name] = [type, value]
        
    def add_child(self, branch):
        self.children.append(branch)
        
    def set_parent(self, parent):
        self.parent = parent
