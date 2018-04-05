import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffled = []
        
        if len(self.nums) != 0:
            parsed_index = {}
            arr_size = len(self.nums)


            while True:
                ind = random.randint(0, arr_size - 1) 

                if ind not in parsed_index:
                    parsed_index[ind] = True
                    shuffled += [self.nums[ind]]

                if len(shuffled) == arr_size:
                    break

        return shuffled