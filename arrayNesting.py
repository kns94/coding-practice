class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        index = {}

        for i in range(len(nums)):
            index[nums[i]] = i 

        subArrays = []
        alreadyparsed = {}

        for i in range(len(nums)):
            current = []
            j = i

            while True:

                if j in alreadyparsed or j not in index:
                    break

                alreadyparsed[j] = True
                current += [nums[j]]
                j = index[j]

            subArrays += [len(current)]

        return max(subArrays)

nums = [5,4,0,3,1,6,2]
print Solution().arrayNesting(nums)