class Solution:
    # Dynamic programming
    # Time complexity O(N)
    # Space complexity O(1)
    # The alogrithm is straightforwrd.
    # We iterate backwards over all the rows in the grid and calculate a total cost for each cell.
    def minCost(self, costs):
        for n in reversed(range(len(costs) -1)):
            # Total cost of painting nth house red.
            costs[n][0] += min(costs[n+1][1], costs[n+1][2])
            # Total cost of painting nth house green.
            costs[n][1] += min(costs[n+1][0], costs[n+1][2])
            # Total cost of painting nth house blue.
            costs[n][2] += min(costs[n+1][0], costs[n+1][1])

        if len(costs) == 0: return 0
        return min(costs[0])