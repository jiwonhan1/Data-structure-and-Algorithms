class Solution:
    def dominantIndex(self, nums):
        l=max(nums)
        if len([1 for num in nums if 2*num <= l]) == len(nums)-1:
            return nums.index(l)
        else:
            return -1