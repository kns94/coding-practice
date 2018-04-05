# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        sums = self.calculateSums(root, [])[1]
        sums = sorted(sums)
        if len(sums) == 0:
            return []
        else:
            counter = {}
            highest = 0
            for s in sums:
                counter.setdefault(s, 0)
                counter[s] += 1
                highest = max(highest, counter[s])

            sums = []
            for k, v in counter.iteritems():
                if v == highest:
                    sums += [k]

            return sums

    def calculateSums(self, root, sums):

        if root is None:
            return 0, sums

        if root.left is None and root.right is None:
            sums += [root.val]
            return root.val, sums

        leftSum = 0
        rightSum = 0
        leftSumArr = []
        rightSumArr = []

        if root.right:
            rec = self.calculateSums(root.right, [])
            rightSum = rec[0]
            leftSumArr = rec[1]

        if root.left:
            rec = self.calculateSums(root.left, [])
            leftSum = rec[0]
            rightSumArr = rec[1]

        currentSum = rightSum + leftSum + root.val
        return currentSum, (leftSumArr + rightSumArr + [currentSum])

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-3)
print Solution().findFrequentTreeSum(root)