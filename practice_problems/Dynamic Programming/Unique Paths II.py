class Solution(object):
    # Time complexity O(MN)
    # Space complexity O(1)
    def uniquePathsWithObstacles(self, obtacleGrid):
        m = len(obtacleGrid)
        n = len(obtacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination
        if obtacleGrid[0][0] == 1:
            return 0


        # Number of ways of reaching the starting cell = 1
        obtacleGrid[0][0] = 1

        # Filling the vlues for the first column
        for i in range(1, m):
            obtacleGrid[i][0] = int(obtacleGrid[i][0] == 0 and obtacleGrid[i-1][0] ==1)

        for j in range(1, n):
            obtacleGrid[0][j] = int(obtacleGrid[0][j] == 0 and obtacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i-1][j] + cell[i][j-1]
        # i.e. From above and left
        for i in range(1,m):
            for j in range(1,n):
                if obtacleGrid[i][j] == 0:
                    obtacleGrid[i][j] = obtacleGrid[i-1][j] + obtacleGrid[i][j-1]
                else:
                    obtacleGrid[i][j] = 0

        return obtacleGrid[m-1][n-1]
