class Solution:
    # Time complexity O(N)
    # Space complexity O(1)
    def myPow(self, x, n):
        N = n
        if n == 0:
            return 1
        elif N < 0:
            x = 1 / x
            N = -N

        ans = 1
        for i in range(N):
            ans = ans * x
        return ans
    # Time complexity O(logN)
    # Space complexity O(logN)
    def fastPow(self, x , n):
        if n == 0:
            return 1
        half = self.fastPow(x, n / 2)
        if (n%2 == 0):
            return half * half
        else:
            return half * half * x

    def myPow2(self, x, n):
        N = n
        if (N < 0):
            x = 1 / x
            N = -N
        return self.fastPow(x, N)
