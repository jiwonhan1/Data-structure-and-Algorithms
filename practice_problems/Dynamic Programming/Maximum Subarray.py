class Solution(object):
    # Optimized Brute Force
    # Time complexity O(N2) Space complexity O(1)
    def maxSubarray(self, nums):
        max_subarray = float('-inf')
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i,len(nums)):
                current_subarray += nums[j]
                max_subarray = max(current_subarray, max_subarray)
        return max_subarray

    # Dynamic Programming
    # Time complexity O(N) Space complexity O(1)
    def maxSubarray2(self, nums):
        # current_subarray: keep the running count of the current subarray we are focusing
        # max_subarray: our final return value. continuously update it whenever we find a bigger subarray
        current_subarray = max_subarray = nums[0]

        for num in nums[1:]:
            current_subarray = max(num, current_subarray+num)
            max_subarray = max(current_subarray, max_subarray)
        return max_subarray