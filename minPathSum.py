class Solution(object):

    def findPath(self, i, j, grid, tracker):
        """Recursively traverse the grid"""
        r, c = len(grid), len(grid[0])

        if i == (r - 1) and j == (c - 1):
            tracker[(i, j)] = grid[i][j]
            return tracker[i, j]

        if (i < 0 or i >= r) or (j < 0 or j >= c):
            return float('inf')

        if (i, j) in tracker:
            return tracker[i, j]

        down = self.findPath(i + 1, j, grid, tracker)
        right = self.findPath(i, j + 1, grid, tracker)
        tracker[i, j] = grid[i][j] + min(down, right)
        return tracker[i, j]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        return self.findPath(0, 0, grid, {})

grid = [[1,3,1], [1,5,1], [4,2,1]]
#print len(grid), len(grid[0])
#print grid[0][0]
print Solution().minPathSum(grid)