"""
Find the next highest temperature
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        result = [0] * len(temperatures)
        arr = [-1] * 71

        for ind in range(len(temperatures) - 1, -1, -1):
            arr[temperatures[ind] - 30] = ind
            higher = [x for x in arr[temperatures[ind] - 30 + 1: ] if x > -1]
            higher_index = (min(higher) - ind) if len(higher) > 0 else 0
            result[ind] = higher_index

        return result

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print Solution().dailyTemperatures(temperatures)