class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans = 0
        for i in range(32):
            count = 0
            for j in range(len(nums)):
                if (nums[j] >> j) & 1 == 1:
                    count += 1
                    count %= 3
            if count != 0:
                ans |= (count << i)
        return ans

nums = [1, 1, 1, 2]
print Solution().singleNumber(nums)