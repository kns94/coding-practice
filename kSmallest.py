# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        current = root
        s = []

        while True:

            if current:
                s += [current]
                current = current.left
            else:
                if len(s) > 0:
                    current = s.pop()
                    k -= 1
                    if k == 0:
                        return current.val

                    current = current.right
                else:
                    break

    def dfs(self, root):

        if root is None:
            return []

        return self.dfs(root.left) + [root.val] + self.dfs(root.right)

root = TreeNode(10)
root.left = TreeNode(6)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)
root.right = TreeNode(12)
root.right.left = TreeNode(11)
root.right.right = TreeNode(15)

print Solution().kthSmallest(root, 2)

