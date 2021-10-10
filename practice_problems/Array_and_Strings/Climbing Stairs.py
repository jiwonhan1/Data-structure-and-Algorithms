class Solution(object):
    def clibStarts(self, n):
        # Fibo with memorization
        # Time complexity O(N) Space complexity O(N)
        dp = {
            1:1,
            2:2
        }

        for i in range(3, n+1):
            dp[i] = dp[i-1] - dp[i-2]
        return dp[n]
