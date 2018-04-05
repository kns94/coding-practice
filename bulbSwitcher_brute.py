class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        bulbs = [0] * n

        for i in range(n):

            j = i

            while j < n:

                if bulbs[j] == 0:
                    bulbs[j] = 1
                else:
                    bulbs[j] = 0

                j += (i + 1)

        return sum(bulbs)

print(Solution().bulbSwitch(3))