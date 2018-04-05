"""
Find if the tree is balanced or not
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printTree(root):

    if root:
        print root.val

    if root.left:
        printTree(root.left)

    if root.right:
        printTree(root.right)

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.calculateNodeHeight(root)[1]

    def calculateNodeHeight(self, node):
        """
        Calculate height of all the nodes and check the difference between two nodes
        """

        if not node.left and not node.right:
            return 1, True

        if node.right and node.left:
            left_rec = self.calculateNodeHeight(node.left)
            leftHeight = left_rec[0]
            balanced_left = left_rec[1]

            right_rec = self.calculateNodeHeight(node.right)
            rightHeight = right_rec[0]
            balanced_right = right_rec[1]

            if abs(rightHeight - leftHeight) > 1:
                balanced = False
            else:
                balanced = balanced_left and balanced_right

            height = 1 + max(rightHeight, leftHeight)

        if not node.right:
            rec = self.calculateNodeHeight(node.left)
            height = 1 + rec[0]
            balanced = rec[1]

            if height > 1:
                balanced = False

        if not node.left:
            rec = self.calculateNodeHeight(node.right)
            height = 1 + rec[0]
            balanced = rec[1]

            if height > 1:
                balanced = False

        return height, balanced

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.right.right = TreeNode(6)
root.right.left = TreeNode(4)
root.right.right.right = TreeNode(7)
root.right.right.right.right = TreeNode(8)

#printTree(root)

print Solution().isBalanced(root)