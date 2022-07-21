from functools import lru_cache
class Solution:
    # Top-down Implementation
    def maxProfit(self, k, prices):
        @lru_cache(None)
        def dp(i, transactions_remaining, holding):
            if transactions_remaining == 0 or i == len(prices):
                return 0

            do_nothing = dp(i+1, transactions_remaining,holding)
            do_something = 0

            if holding:
                #Sell stock
                do_something = prices[i] + dp(i+1, transactions_remaining-1, 0)
            else:
                #Buy stock
                do_something = -prices[i] + dp(i+1,transactions_remaining, 1)
            return max(do_nothing, do_something)
        return dp(0,k,0)