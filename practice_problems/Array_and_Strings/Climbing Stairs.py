class Solution(object):
    # Brute Force
    # Time complexity O(2#n) Space complexity O(N)
    def climbStairs(self,n):
        def climb_stairs(i,n):
            if i > n:
                return 0
            if i == n:
                return 1
            return climb_stairs(i+1, n) + climb_stairs(i+2, n)
        return climb_stairs(0, n)
    # Recursion with Memoization
    # Time complexity O(N)
    # Space complexity O(N)
    def climbStaris(self,n):
        memo = {}
        def climb_staris(i,n):
            if i in memo and memo[i] > 0:
                return memo[i]
            if i > n:
                return 0
            if i == n:
                return 1
            memo[i] = climb_staris(i+1, n) + climb_staris(i+2,n)
            return memo[i]
        return climb_staris(0, n)

    # Fibo with memorization
    # Time complexity O(N) Space complexity O(N)
    def climbStairs(self, n):
        dp = {
            1:1,
            2:2
        }

        for i in range(3, n+1):
            dp[i] = dp[i-1] - dp[i-2]
        return dp[n]
