class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        target = sum(nums)
        if target % 2 != 0:
            return False
        else:
            target = target/2
            nums = sorted(nums)
            for num in nums:
                if num > target:
                    return False
            return self.exploreCombinations(nums, [], len(nums) - 1, target, False)

    def exploreCombinations(self, nums, path, index, target, result):

        if target < 0 or index < 0:
            return False

        if target == 0:
            return True

        for i in range(index, -1, -1):
            result = result or self.exploreCombinations(nums, path + [nums[i]],
                                i - 1, target - nums[i], result)
            if result == True:
                return result
        return result

nums = [4, 5, 5, 6]
nums = [1, 2, 5]
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]
#nums = [28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,42,26,8,87,99,1,16,79]
print Solution().canPartition(nums)