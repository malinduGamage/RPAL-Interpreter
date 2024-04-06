class ControlStructureElement:
    def __init__(self, type, value, bounded_variable=None, env=None):
        self.type = type
        self.value = value
        self.bounded_variable = bounded_variable
        self.env = env
