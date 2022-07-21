class Solution:

    # Approach 1: Top-Down Dynamic Programming (Recursion + Memoization)
    # Time complexity O(N)
    # Space complexity O(N)
    def numWays(self, n, k):
        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k

            if i in memo:
                return memo[i]

            memo[i] = (k-1) * (total_ways(i-1) + total_ways(i-2))
            return memo[i]
        memo = {}
        return total_ways(n)

    # Approach 2: Bottom-Up Dynamic Programming (Tabulation)
    # Time complexity O(N)
    # Space complexity O(N)
    def numWays(self, n, k):
        if n == 1:
            return k
        if n == 2:
            return k * k

        total_ways = [0] * (n + 1)
        total_ways[1] = k
        total_ways[2] = k*k
        for i in range(3, n+1):
            total_ways[i] = (k-1) * (total_ways[i-1] + total_ways[i-2])
        return total_ways[n]