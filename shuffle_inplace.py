import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.original = nums[:]
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        arr_size = len(self.nums)

        if arr_size != 0:

            for i in range(arr_size):
                j = random.randint(0, arr_size - 1)
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums

nums = [1, 2, 3, 4]
obj = Solution(nums)
print obj.shuffle()
print obj.reset()
print obj.shuffle()