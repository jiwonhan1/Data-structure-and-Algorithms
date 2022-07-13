from functools import lru_cache
class Solution:
    # Top down DP
    # Time complexity O(N * amount), where N <= 12 is number of kinds of coins,
    # Space complexity O(amount)
    def coinChange(self, coins, amount):
        @lru_cache(None)
        def dp(i, amount):
            if amount == 0:
                return 0
            if i == -1:
                return float('inf')

            ans = dp(i-1,amount)
            if amount >= coins[i]:
                ans = min(ans, dp(i, coins[i]) +1)
            return ans
        n= len(coins)
        ans = dp(n-1, amount)
        return ans if ans != float('inf') else -1
    # Top down DP - space optimized
    def coinChange(self, coins, amount):
        @lru_cache(None)
        def dp(amount):
            if amount == 0:
                return 0

            ans = float('inf')
            for coin in coins:
                if amount >= coin:
                    ans = min(ans, dp(amount-coin) +1)
            ans = dp(amount)
            return ans if ans != float('inf') else -1

