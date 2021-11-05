class Solution(object):
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