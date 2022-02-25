from collections import deque
class Solution:
    # BFS
    def numIslands(self,grid):
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])
        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"

                    dq = deque([])
                    dq.append((r,c))

                    while dq:
                        row, col = dq.popleft()

                        if row-1 >= 0 and grid[row-1][col] == "1":
                            grid[row-1][col] = "0"
                            dq.append((row-1, col))
                        if row+1 < rows and grid[row+1] [col] == "1":
                            grid[row+1][col] = "0"
                            dq.append((row+1, col))
                        if col-1 >= 0 and grid[row][col-1] == "1":
                            grid[row][col-1] = "0"
                            dq.append((row, col -1))
                        if col+1 < cols and grid[row][col+1] == "1":
                            grid[row][col+1] = "0"
                            dq.append((row, col +1))
        return num_islands

    # DFS
    def numIslands2(self,grid):
        def markIsland(x,y,r,c):
            if x < 0 or y < 0 or y >= c or x >= r or grid[x][y] != "0":
                return

            grid[x][y] = "0"

            markIsland(x+1,y,r,c)
            markIsland(x,y+1,r,c)
            markIsland(x-1,y,r,c)
            markIsland(x,y-1,r,c)

        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    markIsland(i,j,rows,cols)
        return count