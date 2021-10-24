class Solution(object):
    # Time complexity O(M * N)
    def setZeros(self, matrix):
        R = len(matrix)
        C = len(matrix[0])

        rows, cols = set(), set()

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0

    def setZeros(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(R):
            for j in range(C):
                if i in rows or j in rows:
                    matrix[i][j] == 0