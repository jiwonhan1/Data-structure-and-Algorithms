class Solution(object):
    # Time complexity : O(N + M + max(N, M))
    # Space complexity: O(N + M)
    def compareVersion(self, version1, version2):
        num1 = version1.split('.')
        num2 = version2.split('.')
        n1, n2 = len(num1), len(num2)

        for i in range(max(n1, n2)):
            i1 = int(num1[i]) if i < n1 else 0
            i2 = int(num2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        return 0