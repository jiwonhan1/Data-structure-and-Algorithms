class Solution:
    # Brute Force
    # Time complexity O(N)
    # Space complexity O(1)
    # If n < 0, we can substitute x, n with 1/x, -n to make sure n >= 0
    # We need to take care of the corner cases, especially different range limits for negative and positive integers
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

    # Fast Power Algorithm Recursive
    # Assume we have got the result of x(n/2), and now we want to get the result of x(n).
    # Let A be result of x(n/2), we can talk about x(n) based on the parity of n respectively
    # If n is even, we can use formula xn(2) = x(2*n) to get x(n) = A*A. If n is odd, then A*A = x(n-1)
    # Intuitively, we need to multiply another x to get the result, x(n) = A * A * x
    # This approach can be easily implemented using recursion.
    # We call this method "Fast Power", because we only need at most O(logn) computations to get x(n)
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
