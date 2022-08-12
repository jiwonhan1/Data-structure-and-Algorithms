class Solution(object)
    # Brute Force
    # Time complexity O(N2)
    # Space complexity O(1)
    def maxProfit(self, prices):
        max_profit = 0

        for i in range(len(prices) -1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
    # One Pass
    # We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit obtained so far respectively
    # Time complexity O(N) Space complexity O(1)
    def maxProfit(self, prices):
        minprice = float('inf')
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit