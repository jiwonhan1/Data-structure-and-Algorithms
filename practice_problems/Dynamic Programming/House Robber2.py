
# Approach 1: Recursion with Memoization

# Algorithm:
# 1. WE define a function called robFrom() which takes the index of the house that the robbr currently has to examine.
# Also, this function takes the nums array which is required during the calculations.

# 2. At each step of our recursive call, the robber has two options: He can either rob the current house or not.
# 1) If the robber chooses to rob the current house, then he have to skip the next house i.e robFrom(i+2, nums).
# The answer here would be whatever is returned by robFrom(i+2, nums) in addition to the amount that the robber will get by robbing the current house i.e nums[i]
# Otherwise, he can simply move on to the house next door and return whatever profit he will make in the sub-problem i.e. robFrom(i+1, nums)
# 3. We need to find, cache, and return the maximum of these two options at each step.
# robFrom(0, nums) will give us the answer to the entire problem.
# Time complexity O(N) since we process at most N recursive calls
# Space complexity O(N) which is occupied by the cache and also by the recursion stack.
class Solution:

    def __init__(self):
        self.memo = {}

    def rob(self, nums):
        self.memo = {}

        return self.robFrom(0, nums)

    def robFrom(self, i, nums):

        if i >= len(nums):
            return 0

        if i in self.memo:
            return self.memo[i]

        ans = max(self.robFrom(i+1, nums), self.robFrom(i+2, nums) + nums[i])

        self.memo[i] = ans

        return ans

# Approach 2: Dynamic Programming
# Time complexity O(N) since we have loop from N-2 ... 0
# Space complexity O(N) which is used by the table.
class Solution2:
    def rob(self, nums):
        if not nums:
            return 0

        # We define a table which we will use to store the results of our sub-problems.
        # Let's call this table maxRobbedAmount where maxRobbedAmount[i] is the same value that would be returned by recurse(i) in the previous solution.

        maxRobbedAmount = [None for _ in range(len(nums) +1)]
        N = len(nums)
        # We set maxRobbedAmount[N] to 0 since this means the robber doesn't have any houses left to rob, thus zero profit.
        # Additionally, we set maxRobbedAmount[N-1] to nums[N-1] because in this case, there is only one house to rob which is the last house. Robbing it will yield the maximum profit.
        maxRobbedAmount[N], maxRobbedAmount[N-1] = 0, nums[N-1]

        for i in range(N-2, -1,-1):
            maxRobbedAmount[i] = max(maxRobbedAmount[i+1], maxRobbedAmount[i+2],nums[i])

        return maxRobbedAmount[0]

# Approach 3: Optimized Dynamic Programming
# Time complexity O(N)
# Space complexity O(1)
class Solution3:
    def rob(self, nums):
        if not nums:
            return 0

        N = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[N-1]

        for i in range(N-2, -1, -1):
            current = max(rob_next, nums[i] + rob_next_plus_one)

            rob_next_plus_one = rob_next
            rob_next = current
        return rob_next

