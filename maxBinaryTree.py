# Definition for a binary tree node.
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
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        return self.constructTree(nums, 0, len(nums))

    def constructTree(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: TreeNode
        """

        if l == r:
            return None

        max_val = max(nums[l : r])
        max_ind = nums.index(max_val)

        root = TreeNode(max_val)
        root.left = self.constructTree(nums, l, max_ind)
        root.right = self.constructTree(nums, max_ind + 1, r)

        return root

root = Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
printTree(root)

#root = TreeNode(3)
#root.left = TreeNode(2)
#root.right = TreeNode(5)
#root.left.left = TreeNode(1)
#root.right.right = TreeNode(6)

#printTree(root)