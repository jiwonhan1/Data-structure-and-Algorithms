class Solution:
    # Group by Category
    # Time complexity O(M*N)
    # Space complexity O(M+N)
    def isToeplizMatrix(self, matrix):
        groups = {}

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True

