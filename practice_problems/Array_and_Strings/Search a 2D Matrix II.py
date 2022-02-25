class Solution(object):
    # Brute Force
    # Time complexity O(nm)
    # Space complexity O(1)
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if target in row:
                return True
        return False

    # # Binary Search
    # def searchMatrix(self, matrix, target):
    #     if not matrix:
    #         return False
    #
    #     for i in range(min(len(matrix)))