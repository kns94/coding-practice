class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if k != len(nums) and k != 0:
            nums = nums[-k:] + nums[:-k]
        
        return nums 

print Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)