class Solution(object):
    def __init__(self):
        self.result = []
        self.seen = {}

    def increasingSubsequences(self, nums, i):

        if i < 0:
            return

        self.seen[i] = [nums[i]]

        i -= 1
        while i >= 0:
            if :
                self.increasingSubsequences(nums, i)
                i -= 1

        return

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.increasingSubsequences(nums, 1)
        print self.seen

nums = [4, 6]
print Solution().findSubsequences(nums) 
