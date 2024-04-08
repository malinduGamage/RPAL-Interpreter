from collections import defaultdict

class Environment:
    index = -1

    def __init__(self, parent=None):
        Environment.index += 1
        self.index = Environment.index
        self._environment = defaultdict(lambda: [None, None])  # name: [type, value]
        self.children = []
        self.parent = parent

        if self.index == 0:
            self._initialize_initial_vars()

    def _initialize_initial_vars(self):
        initial_vars = {
            "Print": ["Print", "Print"],
            "Isstring": ["function", None],
            "Isinteger": ["function", None],
            "Istruthvalue": ["function", None],
            "Istuple": ["function", None],
            "Isfunction": ["function", None],
            "Null": ["function", None],
            "Order": ["function", None],
            "Stern": ["function", None],
            "Stem": ["function", None],
            "ItoS": ["function", None],
            "neg": ["function", None],
            "not": ["function", None],
            "Conc": ["function", None],
        }
        self._environment.update(initial_vars)

    def add_var(self, name, type, value):
        self._environment[name] = [type, value]

    def add_child(self, branch):
        self.children.append(branch)

    def set_parent(self, parent):
        self.parent = parent
        # Update the parent reference in the _environment dictionary
        self._environment['__parent__'] = parent._environment if parent else None
