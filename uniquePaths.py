class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        return self.findUnique(m, n, 0, 0, {})

    def findUnique(self, m, n, i, j, dp):

        if i < 0 or i >= m or j <0 or j >=n:
            return 0

        if i == (m - 1) and j == (n - 1):
            dp[(i, j)] = 1
            return 1

        if (i, j) not in dp:
            rec = self.findUnique(m, n, i, j + 1, dp) +\
                    self.findUnique(m, n, i + 1, j, dp)
            dp[(i, j)] = rec
        return dp[(i,j)]

print Solution().uniquePaths(2, 3)
