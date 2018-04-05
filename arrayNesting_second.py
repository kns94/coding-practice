class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        alreadyparsed = {}
        subArrays = []
        
        for num in nums:
            current = []
            j = num

            while True:
                if j not in alreadyparsed:
                    alreadyparsed[j] = True
                    current += [j]
                    j = nums[j]
                else:
                    break

            subArrays += [len(current)]

        return max(subArrays)

nums = [5,4,0,3,1,6,2]
print Solution().arrayNesting(nums)