class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class NaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, parent_value, value):
        parent_node = self._find_node(self.root, parent_value)
        if parent_node:
            new_node = Node(value)
            parent_node.children.append(new_node)
        else:
            print("Parent value not found.")

    def remove(self, value):
        self.root = self._remove_node(self.root, value)

    def _remove_node(self, current_node, value):
        if current_node is None:
            return None
        if current_node.value == value:
            return current_node.children  # Return the children of the node to replace it in the parent's children list
        new_children = []
        for child in current_node.children:
            new_child = self._remove_node(child, value)
            if new_child:
                if isinstance(new_child, list):
                    new_children.extend(new_child)  # Append individual children
                else:
                    new_children.append(new_child)  # Append a single child
        current_node.children = new_children
        return current_node if current_node.value != value else new_children


    def _find_node(self, current_node, value):
        if current_node.value == value:
            return current_node
        for child in current_node.children:
            found_node = self._find_node(child, value)
            if found_node:
                return found_node
        return None

    def display(self):
        self._display_helper(self.root)

    def _display_helper(self, node, level=0):
        if node:
            print("  " * level + str(node.value))
            for child in node.children:
                self._display_helper(child, level + 1)
