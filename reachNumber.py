class Solution(object):

    def __init__(self):
        self.dp = {}

    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        if target == 0:
            return 0

        self.dp[0] = True
        return self.findWay(target, 0, 0)

    def findWay(self, target, current, count):
        """
        Find minimum number of steps 
        """

        if current in self.dp:
            return self.dp[current]

        if current == target:
            self.dp[current] = count
            return self.dp[current]

        count = count + 1

        if current < target:
            if current + 1 < target:
                self.dp[current] = float('inf')
                return self.dp[current]

        if current > target:
            if current - 1 > target:
                self.dp[current] = float('inf')
                return self.dp[current]

        return min(self.findWay(target, current - count, count), 
            self.findWay(target, current + count, count))


print Solution().reachNumber(3)