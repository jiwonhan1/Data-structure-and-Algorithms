class solution:

    # O(MN)

    def zero_matrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        rows = set()
        cols = set()

        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    rows.add(x)
                    cols.add(y)

        for x in range(m):
            for y in range(n):
                if (x in rows) (y in cols):
                    matrix[x][y] = 0

        return matrix
