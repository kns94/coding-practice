class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        one = nums[:]
        two = nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
            return one == sorted(one) or two == sorted(two) 



nums = [4, 2, 3]
nums = [4, 2, 1]
nums = [2, 3, 3, 2, 4]
nums = [3, 4, 2, 3]
nums = [3, 3, 2, 2]
print Solution().checkPossibility(nums)