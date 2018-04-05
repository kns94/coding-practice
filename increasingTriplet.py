class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 0:
            return False

        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                first = second
            else:
                return True
        return False


nums = [5, 4, 3, 2, 1]
print Solution().increasingTriplet(nums)
