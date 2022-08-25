class Solution():
    # DP
    # Time and space complexity O(MN)
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for j in range(1, m):
            grid[j][0] += grid[j-1][0]

        for i in range(1, m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]

    # DP
    # Space complexity O(1)
    def minPathSum(self, grid):
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if i and j:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i:
                    grid[i][j] += grid[i-1][j]
                elif j:
                    grid[i][j] += grid[i][j-1]
        return grid[-1][-1]

