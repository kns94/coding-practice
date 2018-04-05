# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []

        return self.parseTree(root, {}, 0).values()

    def parseTree(self, node, levels, depth):
       
        if depth not in levels:
            levels[depth] = node.val

        if node.right:
            levels = self.parseTree(node.right, levels, depth + 1)
        if node.left:
            levels = self.parseTree(node.left, levels, depth + 1)

        return levels
        
       
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
#root.right.right = TreeNode(4)

print Solution().rightSideView(root)