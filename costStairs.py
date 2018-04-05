class Solution(object):

    def __init__(self):
        self.dp = {}

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        return min(self.findMinCost(0, cost, 0), self.findMinCost(1, cost, 0))

    def findMinCost(self, ind, cost_arr, current_cost):
        """
        Recursively parse through all indices to find minimum cost
        """
        current_cost += cost_arr[ind]

        if ind in self.dp:
            return self.dp[ind]

        if (ind == len(cost_arr) - 2) or ind == (len(cost_arr) - 1):
            self.dp[ind] = cost_arr[ind]
            return cost_arr[ind]

        self.dp[ind] = cost_arr[ind] + min(self.findMinCost(ind + 1, cost_arr, current_cost), self.findMinCost(ind + 2, cost_arr, current_cost))
        return self.dp[ind]

cost = [10, 15, 20]
print Solution().minCostClimbingStairs(cost)