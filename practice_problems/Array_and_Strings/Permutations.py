class Solution(object):
    def permute(self, nums):
        def backtrack(first =0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[n] = nums[n], nums[first]
                backtrack(first+1)
                nums[first], nums[n] = nums[first], nums[n]
            n = len(nums)
            output = []
            backtrack()
            return output