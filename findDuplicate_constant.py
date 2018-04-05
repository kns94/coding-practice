class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
 
        t = 0
        h = 0

        while True:

            t = nums[t]
            h = nums[nums[h]]

            if t == h:
                break

        t = 0
        while True:
            t = nums[t]
            h = nums[h]

            if t == h:
                break

        return t

nums = [5, 4, 1, 2, 1, 1]
print Solution().findDuplicate(nums)