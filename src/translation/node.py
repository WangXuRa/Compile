class Node:
    def __init__(self, node_type, value=None):
        self.node_type = node_type  # Type of node (e.g., "PROGRAM", "STATEMENT")
        self.value = value          # Value for terminal nodes (e.g., identifier, number)
        self.children : list[Node] = []          # List of child nodes
        self.parent = None

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):
        # if it is not a leaf node, recursively print its leaves
        if self.children:
            ret = "  " * level + "<" + self.node_type + ">" + "\n"
            for child in self.children:
                # print(ret)
                ret += child.__repr__(level + 1)
            ret += "  " * level + "</" + self.node_type + ">" + "\n"
            return ret
        # if it is a leaf node, then only print one line for the node
        else:
            ret = "  " * level + "<" + self.node_type + ">"
            if self.value:
                ret += repr(self.value)[1:-1]
            ret += "</" + self.node_type + ">" + "\n"
            return ret