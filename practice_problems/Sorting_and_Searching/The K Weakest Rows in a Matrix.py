class Solution(object):
    # Linear Search and Sorting
    # Time complexity O(m (n+logm))
    # Space complexity O(m)
    def kWeakestRows(self, mat, k):
        m = len(mat)
        n = len(mat[0])
        strengths = []

        for i, row in enumerate(range(mat)):
            strength = 0
            for j in range(n):
                if row[j] == 0:
                    break
                strength += 1
            strength.append((strength,i))
        strengths.sort()
        indexes = []
        for i in range(k):
            indexes.append(strengths[i][1])
        return indexes
    # Time complexity O(m logmn)
    # Space complexity O(m)
    def kWeakestRows(self, mat, k):
        n = len(mat[0])
        def binary_search(row):
            low = 0
            high = 0
            while low < high:
                mid = low + (high-low) // 2
                if row[mid] == 1:
                    row = mid +1
                else:
                    high = mid
            return low
        row_strengths = []
        for i, row in enumerate(mat):
            row_strengths.append((binary_search(row),i))
        row_strengths.sort()
        indexes = []
        for i in range(k):
            indexes.append(row_strengths[i][1])
        return indexes