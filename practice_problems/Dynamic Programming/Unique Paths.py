class Solution:
    def uniquePaths(self, m, n):

        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    # Dynamic programming
    def uniquePaths(self, m, n):
        # initiate 2D array d[m][n] = number of paths.
        # To start, put number of paths equal to 1 for the first row and the first column
        # For the simplicity, one could initiate the whole 2D array by ones
        # Iterate over all "inner" cells: d[col][row] = d[col-1][row] + d[col][row-1]
        # Return d[m-1][n-1]

        # time complexity O(NM)
        # space complexity O(NM)
        d = [[1] * n for _ in range(m)]
        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col-1][row] + d[col][row-1]
        return d[m-1][n-1]