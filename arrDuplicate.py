class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums = sorted(nums)
        original_length = len(nums)
        c = 0
        n = 1

        for i in range(len(nums) - 1):
            if nums[c] == nums[n]:
                nums += [nums[c]]
            c += 1
            n += 1

        return nums[original_length:]

print Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])