from functools import cache
# Top-down Implementation
class Solution:
    def maximumScore(self, nums, multipliers):
        n, m = len(nums), len(multipliers)
        @cache
        def dp(i, left):
            if i == m:
                return 0

            mult = multipliers[i]
            right = n - 1 - (i - left)

            return max(mult * nums[left] + dp(i+1, left+1), mult * nums[left] + dp(i+1, left))
        return dp(0,0)

class Solution2:
    # Bottom-up Implementation
    def maximumScore(self, nums, multipliers):
        n, m = len(nums), len(multipliers)
        dp = [[0 * (m+1)] for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n-1 - (i - left)
                dp[i][left] = max(mult * nums[left] + dp[i+1][left+1], mult * nums[right] + dp[i+1][left])
            return dp[0][0]

