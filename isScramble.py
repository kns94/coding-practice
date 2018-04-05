class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        """Initial instances"""
        self.tree1 = None
        self.tree2 = None

    def createTree(self, arr):
        """Given an array, construct a tree and return it"""
        
        if len(arr) == 1:
            return TreeNode(arr[0])

        mid = int(len(arr)/2)

        left_child = self.createTree(arr[ : mid])
        right_child = self.createTree(arr[mid : ])

        root = TreeNode(left_child.val + right_child.val)
        root.left = left_child
        root.right = right_child

        return root

    def modifyTree(self, root):
        """Given a tree, modify the root value after changes in leaves"""
        
        if root is None:
            return ''

        if root.left is None and root.right is None:
            return root

        root.val = self.modifyTree(root.left).val + self.modifyTree(root.right).val
        return root

    def printTree(self, root):
        """In order traversal of tree"""

        if root is None:
            return ['*']

        return [root.val] + self.printTree(root.left) + self.printTree(root.right)

    def scrambleTree(self, root1, root2):
        """Scramble trees to check if they are similar. I will alway modify tree2"""

        """Checking if root values themselves are same"""
        if root1.val == root2.val:
            return 

        """Checking if exactly reverse tree exists"""
        if root1.val == root2.val[: : -1]:
            root2.left, root2.right = root1.left, root1.right
            self.modifyTree(self.tree2)
            return

        """Checking if both children are same"""                        #This could be redundant, remove if required
        if root1.left.val == root2.left.val and root2.right.val == root2.right.val:
            return

        """Now, this siginifies an instance both children are at opposite ends"""
        if root1.left.val == root2.right.val and root1.right.val == root2.left.val:
            root2.left, root2.right = root2.right, root2.left
            self.modifyTree(self.tree2)
            return

        elif sorted(root1.left.val) == sorted(root2.right.val) and sorted(root1.right.val) == sorted(root2.left.val):
            root2.left, root2.right = root2.right, root2.left
            self.modifyTree(self.tree2)

        found = False
        if sorted(root1.left.val) == sorted(root2.left.val):
            self.scrambleTree(root1.left, root2.left)
            found = True

        if sorted(root1.right.val) == sorted(root2.right.val):
            #print(root1.right.val, root2.right.val)
            self.scrambleTree(root1.right, root2.right)
            found = True

        """If the result could be achieved by reversing trees"""
        if root2.right.val + root2.left.val == root1.val:
            root2.left, root2.right = root2.right, root2.left
            self.modifyTree(self.tree2) 
                
        return

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if sorted(s1) != sorted(s2):
            return False

        #if s1 == s2:
        #    return True

        self.tree1 = self.createTree(s1)
        self.tree2 = self.createTree(s2)
        self.scrambleTree(self.tree1, self.tree2)
        #print(self.tree1.val, self.tree2.val)
        return self.tree1.val == self.tree2.val

        #print(self.printTree(self.tree1))
        #self.tree1.left, self.tree1.right = self.tree1.right, self.tree1.left
        #self.modifyTree(self.tree1)
        #print(self.printTree(self.tree1))

if __name__ == "__main__":

    s1 = 'abb'
    s2 = 'bab'

    print(Solution().isScramble(s1, s2))
