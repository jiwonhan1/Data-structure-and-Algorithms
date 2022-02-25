class Tri:
    def __init__(self):
        def helper(k):
            if k == 0:
                return 0
            if nums[k]:
                return nums[k]
            nums[k] = helper(k-1) + helper(k-2) + helper(k-3)
            n = 38
            self.nums = nums = [0] * n
            nums[1] = nums[2] = 1
            helper(n-1)

class Solution(object):
    # Space Optimisation : Dynamic Programming
    # Time complexity O(N)
    def tribonacci(self, n):
        if n < 3:
            return 1 if n else 0
        x,y,z = 0, 1, 1
        for _ in range(n -2):
            x,y,z = y,z,x+y+z
        return z
    # Performance Optimisation : Recursion with Memoization
    # Time comlexity O(1)
    t = Tri()
    def tribonacci(self, n):
        return self.t.nums[n]