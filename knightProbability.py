class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        
        return self.exploreBoard(N, K, r, c)

    def exploreBoard(self, N, k, i, j):
        """
        Calculate probability somehow
        """

        print k, i, j
        if i < 0 or j < 0 or i >= N or j >= N:
            return 0

        if k == 0:
            return 1

        count = 0
        for step in [(1, -2), (1, 2), (2, -1), (2, 1), (-1, -2),
                         (-1, 2), (-2, -1), (-2, 1)]:
            dr, dc = step[0], step[1]

            if (i + dr) >= 0 and (i + dr) < N and (j + dc) >= 0 and (j + dc) < N:
                count += 1

        combinations = (count * 1.0)/8
        print combinations

        prob = 0
        for step in [(1, -2), (1, 2), (2, -1), (2, 1), (-1, -2),
                         (-1, 2), (-2, -1), (-2, 1)]:
            dr, dc = step[0], step[1]

            if (i + dr) >= 0 and (i + dr) < N and (j + dc) >= 0 and (j + dc) < N:
                prob += combinations * self.exploreBoard(N, k - 1, i + dr, j + dc)

        return prob
N = 3
K = 2
r = 0
c = 0
print Solution().knightProbability(N, K, r, c)