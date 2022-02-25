class Solution(object):
    # Using two pointers
    # Time complexity O(N) Space complexity O(1)
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        ans = float('inf')
        left = 0
        sum = 0
        for i in range(n):
            sum += nums[i]
            while sum >= target:
                ans = min(ans, i+1 -left)
                sum -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0