class Solution:
    # Bottom-up Implementation
    def rob(self, nums):
        if not nums:
            return 0
        dp = [0] * len(nums)

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

    # Top-down Implementation
    def rob(self, nums):
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i] = max(dp(i-1), nums[i] + dp(i-2))
            return memo[i]
        memo = {}
        return dp(len(nums -1))