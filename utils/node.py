class Node:
    """
    A node in a binary tree data structure.

    A node contains a data field and a list of child nodes.
    """
    def __init__(self, data):
        """
        Initialize a new node with the given data.

        Args:
            data (object): The data stored in the node.
        """
        # Initialize the Node object with the provided data
        self.data = data
        # Initialize an empty list to store the children nodes
        self.children = []

    def add_child(self, child):
        """
        Add a child node to the current node.

        Args:
            child (Node): The child node to add.
        """
        # Add a child node to the current node's children list
        # The child is added at index 0 to ensure that the most recently added child appears first
        self.children.insert(0, child)

    def remove_child(self, child):
        """
        Remove a child node from the current node.

        Args:
            child (Node): The child node to remove.
        """
        # Check if the provided child exists in the children list
        if child in self.children:
            # If the child exists, remove it from the children list
            self.children.remove(child)
        else:
            # If the child does not exist, print a message indicating that it was not found
            print("Child not found")

    def __repr__(self):
        """
        Return a string representation of the node.

        Returns:
            str: The string representation of the node.
        """
        # String representation of the node, showing its data and the data of its children
        children_data = ", ".join(str(child.data) for child in self.children)
        return f"Node(data={self.data}, children=[{children_data}])"
