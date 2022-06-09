from functools import cache
class Solution:
    # Bottom-up dynamic programming
    # Time and space complexity O(N)
    def minCostClimbingStairs(self, cost):
        minimum_cost = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            take_one_step = minimum_cost[i-1] + cost[i-1]
            take_two_step = minimum_cost[i-2] + cost[i-2]
            minimum_cost[i] = min(take_two_step, take_one_step)
        return minimum_cost[-1]
    # Top-down dynamic programming
    # Time and space complexity O(N)
    def minCostClimbingStairs(self,cost):
        def minimum_cost(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            down_one = cost[i-1] + minimum_cost(i-1)
            down_two = cost[i-2] + minimum_cost(i-2)
            memo[i] = min(down_two, down_one)
            return memo[i]
        memo = {}
        return minimum_cost(len(cost))

    def minCostClimbingStairs(self,cost):
        # In Python, functools module contains functions that can be used to automatically memoize a function
        @cache
        def minimum_cost(i):
            if i <=1: return 0

            down_one = cost[i-1] + minimum_cost(i-1)
            down_two = cost[i-2] + minimum_cost(i-2)
            return min(down_one, down_two)
        return minimum_cost(len(cost))

    # Bottom-Up, Constant Space
    # Time complexity O(N)
    # Space complexity O(1)
    def minCostClimbingStairs(self, cost):
        down_one = down_two = 0
        for i in range(2, len(cost) +1):
            temp = down_one
            down_one = min(down_one+cost[i-1],down_two+cost[i-2])
            down_two = temp
        return down_one