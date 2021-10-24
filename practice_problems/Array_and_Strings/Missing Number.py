class Solution(object):
    # Time complexity O(N) Space complexity O(N)
    def missingNumber(self, nums):
        num_set = set(nums)
        number = len(nums) + 1
        for n in range(number):
            if n not in num_set:
                return n
