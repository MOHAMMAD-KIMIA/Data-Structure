class BinaryTree:
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    # Constructor
    def __init__(self):
        self.root = None 
            
    def insertRec(self, root, val):
        if root is None:
            return self.TreeNode(val)  
        if val < root.data:
            root.left = self.insertRec(root.left, val) 
        elif val > root.data:
            root.right = self.insertRec(root.right, val)  
        return root
    
    def insert(self, val):
        self.root = self.insertRec(self.root, val)

    # Helper function to find the rightmost node in the left subtree
    def rightMin(self, root):
        temp = root
        while temp.left is not None:
            temp = temp.left
        return temp.data
       
    def remove(self, val):
         self.root = self._remove(self.root, val)

    def _remove(self, root, val):
        if root is None:
            return None

        if val < root.data:
            root.left = self._remove(root.left, val)
        elif val > root.data:
            root.right = self._remove(root.right, val)
        else:
            if root.left is None and root.right is None:
                del root
                return None
            elif root.left is None:
                temp = root.right
                del root
                return temp
            elif root.right is None:
                temp = root.left
                del root
                return temp
            else:
                right_min = self.rightMin(root.right)
                root.data = right_min
                root.right = self._remove(root.right, right_min)
        return root

    def search(self, val):
        return self.searchRec(self.root, val)

    def searchRec(self, root, val):
        if root is None or root.data == val:
            return root
        if val < root.data:
            return self.searchRec(root.left, val)
        return self.searchRec(root.right, val)
    
    def printInorder(self, root):
        if root is not None:
            self.printInorder(root.left) 
            print(root.data, end=" ")
            self.printInorder(root.right)

    def inOrder(self):
        self.printInorder(self.root)
        
    def printPreorder(self, root):
        if root is not None:
            print(root.data, end=' ')  
            self.printPreorder(root.left) 
            self.printPreorder(root.right)
            
    def preOrder(self):
        self.printPreorder(self.root)
    
    def printPostorder(self, root):
        if root is not None:
            self.printPostorder(root.left) 
            self.printPostorder(root.right) 
            print(root.data, end=' ')  
            
    def postOrder(self):
        self.printPostorder(self.root)

# Create a binary tree
binary_tree = BinaryTree()

# Test insertion
values_to_insert = [50, 30, 70, 20, 40, 60, 80]
for value in values_to_insert:
    binary_tree.insert(value)

# Test inorder traversal
print("Inorder traversal:")
binary_tree.inOrder()
print()  # Add a newline for better readability

# Test preorder traversal
print("Preorder traversal:")
binary_tree.preOrder()
print()  # Add a newline for better readability

# Test postorder traversal
print("Postorder traversal:")
binary_tree.postOrder()
print()  # Add a newline for better readability

# Test searching
values_to_search = [30, 55, 80, 10]
for value in values_to_search:
    result = binary_tree.search(value)
    if result:
        print(f"Value {value} found in the tree.")
    else:
        print(f"Value {value} not found in the tree.")

# Test removal
values_to_remove = [30, 55, 80, 10]
for value in values_to_remove:
    binary_tree.remove(value)
    print(f"Value {value} removed. Inorder after removal:")
    binary_tree.inOrder()
    print()  # Add a newline for better readability
