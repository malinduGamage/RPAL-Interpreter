class ControlStructureElement:
    def __init__(self, type, value, bounded_variable=None,control_structure=None, env=None , operator=None):
        self.type = type
        self.value = value
        self.bounded_variable = bounded_variable
        self.control_structure = control_structure
        self.env = env
        self.operator = operator
