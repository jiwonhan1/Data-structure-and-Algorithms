class Solution:
    # Sliding Window
    # Time complexity O(N)
    # Space complexity O(1)
    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor +1)
        return ans