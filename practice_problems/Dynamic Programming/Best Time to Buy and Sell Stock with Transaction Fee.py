class Solution:
    # Dynamic Programming
    # Time complexity O(N)
    # Space complexity O(1)
    # To transition from the i-th day to the i+1-th day, we either sell our stock cash=max(cash, hold+prices[i]-fee)
    # or buy a stock hold = max(hold, cash-prices[i]).
    # At the end, we want to return cash
    # We can transform cash first without using temporary variables because selling and buying on the same day can't be better than just continuting to hold the stock.
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold+prices[i]-fee)
            hold = max(hold, cash-prices[i])
        return cash