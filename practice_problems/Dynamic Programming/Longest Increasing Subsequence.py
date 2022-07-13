class Solution:
    # Dynamic Programming
    # Time complexity O(N2)
    # Space complexity O(N)
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    # Intelligently Build a Subsequence
    # Time complexity O(N)
    # Space complexity O(N)
    def lengthOfLIS(self, nums):
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(nums)
            else:
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num
        return len(sub)
