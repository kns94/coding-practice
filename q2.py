"""
Zillow Hiring Test Question 1: Given a ternary tree where left child is smaller than the root. Middle child is equal to the root and the
right child is greater than the root - design algorithms to add nodes and remove nodes. I have to rebalance the tree afterwords!

Input: Functions to insert or delete a node
Output: Modified tree structure

Rules for deletion:
    1. If the node to delete is a leaf node, delete it 
    2. If the node to delete has a mid child, traverse the mid child and delete according to the rules.
    2. If the node to delete has only a left child - replace node with the left child
    3. If the node to delete has only a right child or has both left and right child - replace root with smallest value in right child and delete
    the node in right sub-tree
"""


class Node(object):  # Please do not remove or rename any of this code
    """Represents a single node in the Ternary Search Tree"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.mid = None
        self.right = None

class Tree(object):  # Please do not remove or rename any of this code
    """The Ternary Search Tree"""
    def __init__(self):
        self.root = None

    # Please complete this method.
    """Inserts val into the tree. There is no need to rebalance the tree."""
    def insert(self, val):
        
        if self.root is None:
            """Create root!"""
            self.root = Node(val)
        else:
            """Recursively add nodes to the tree"""
            self.insertNode(self.root, val)

    def insertNode(self, root, val):
        """I created this method to recursively add children to the tree. Given a root and value!"""

        if root.val == val:
            """If the new value is same as root"""
            if root.mid is None:
                root.mid = Node(val)
            else:
                self.insertNode(root.mid, val)

        if val < root.val:
            """If the new value is less than root"""
            if root.left is None:
                root.left = Node(val)
            else:
                self.insertNode(root.left, val)

        if val > root.val:
            """If the new value is more than root"""
            if root.right is None:
                root.right = Node(val)
            else:
                self.insertNode(root.right, val)
 
    # Please complete this method.
    """Deletes only one instance of val from the tree.
       If val does not exist in the tree, do nothing.
       There is no need to rebalance the tree."""
    def delete(self, val):
        
        if self.root is None:
            return None
        else:
            if val == self.root.val:
                #The value to be deleted matches the root value
                if self.root.mid is None:
                    #If the middle node does not exist
                    if self.root.left is None and self.root.right is None:
                        #If the root is a leaf
                        self.root = None
                    elif self.root.right is None:
                        #If right child does not exist, set root as left sub-tree
                        self.root = self.root.left
                    else:
                        #If the left child does not exist, set root as minumum of right-subtree
                        min_right = self.findMin(self.root.right)
                        self.deleteNode(self.root, self.root.right, min_right)
                        self.root.val = min_right
                else:
                    self.deleteNode(self.root, self.root.mid, val)
            elif val < self.root.val:
                self.deleteNode(self.root, self.root.left, val)
            elif val > self.root.val:
                self.deleteNode(self.root, self.root.right, val)

    def deleteNode(self, parent, child, val):
        """Recursively deleting a node, if it exists"""

        if child is None:
            return None

        if val < child.val:
            self.deleteNode(child, child.left, val)
        elif val > child.val:
            self.deleteNode(child, child.right, val)
        elif child.val == val:
            #If child's value matches the value to be deleted
            if child.mid is None:
                if child.left is None and child.right is None:
                    #If child is leaf
                    if val > parent.val:
                        parent.right = None
                    elif val < parent.val:
                        parent.left = None
                    elif val == parent.val:
                        parent.mid = None

                elif child.right is None:
                    #Only left child of child is present
                    if val < parent.val:
                        parent.left = child.left
                    elif val > parent.val:
                        parent.right = child.left

                else:
                    #Both children are present or only right child is present
                    min_right = self.findMin(child.right)
                    self.deleteNode(child, child.right, min_right)
                    child.val = min_right

            else:
                self.deleteNode(child, child.mid, val)
            

    def findMin(self, root):
        """Given a tree, find minimum value in that tree"""

        if not root:
            #If root does not exist, return NULL
            return None
        else:

            if root.left is not None:
                #If left child exists, recursively find smallest value of left subtree
                return self.findMin(root.left)
            else: 
                #If middle child exists, only right child exists or if the root is leaf - return root value
                return root.val

    def printTree(self, root):
        """Recursively printing tree for debugging"""

        if not root:
            return ['NULL']
        else:
            return [root.val] + self.printTree(root.left) + self.printTree(root.mid) + self.printTree(root.right)

if __name__ == "__main__":
    tree = Tree()
    #tree.insert(5)
    #tree.insert(4)
    #tree.insert(9)
    #tree.insert(7)
    #tree.insert(2)
    #tree.insert(2)

    #tree.insert(3)
    #tree.insert(3)
    #tree.insert(1)
    #tree.insert(4)

    #tree.insert(7)
    #tree.insert(4)
    #tree.insert(7)
    #tree.insert(8)
    #tree.insert(1)
    #tree.insert(1)
    #tree.insert(-1)
    #tree.insert(2)
    #tree.insert(18)

    #tree.insert(1)
    #tree.insert(2)
    #tree.insert(3)
    #print(tree.printTree(tree.root))
    #tree.delete(2)
    #print(tree.printTree(tree.root))
    #tree.delete(1)
    #print(tree.printTree(tree.root))
    #tree.insert(4)
    #print(tree.printTree(tree.root))

    tree.insert(50)
    tree.insert(39)
    tree.insert(25)
    tree.insert(30)
    tree.insert(50)
    tree.insert(70)
    tree.insert(60)
    tree.insert(90)
    tree.insert(100)
    tree.insert(95)
    tree.insert(105)
    tree.insert(100)
    tree.insert(26)
    tree.insert(28)
    tree.insert(29)

    #print(str(tree.printTree(tree.root)) + '\n')

    print(str(tree.printTree(tree.root)) + '\n')
    tree.delete(50)
    tree.delete(50)
    print(str(tree.printTree(tree.root)) + '\n')
    #tree.delete(76)
    #print(str(tree.printTree(tree.root)) + '\n')
    #tree.delete(125)
    #print(str(tree.printTree(tree.root)) + '\n')
    #tree.delete(100)
    #print(str(tree.printTree(tree.root)) + '\n')
    
    #print(tree.printTree(tree.root))
    #tree.delete(1)
    #print('\n')
    #print(tree.printTree(tree.root))
    #print(tree.findMin(tree.root))

