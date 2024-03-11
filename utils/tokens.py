class Token :
    def __init__(self, value, type_):
        # Initialize the Token with the specified type and value
        self.type = type_
        self.value = value

    def get_type(self):
        # Get the type of the token
        return self.type

    def get_value(self):
        # Get the value of the token
        return self.value

    def set_type(self, type_):
        # Set the type of the token
        self.type = type_

    def set_value(self, value):
        # Set the value of the token
        self.value = value

    def __str__(self):
        # Return a string representation of the token
        return "<{}: {}>".format(self.type, self.value)

    def __repr__(self):
        # Return an unambiguous string representation of the token
        return "<{}: {}>".format(self.type, self.value)

    def __eq__(self, other):
        # Define equality comparison between two tokens
        return self.type == other.type and self.value == other.value

    def __ne__(self, other):
        # Define inequality comparison between two tokens
        return not self.__eq__(other)

    def __hash__(self):
        # Return a hash value for the token
        return hash((self.type, self.value))

