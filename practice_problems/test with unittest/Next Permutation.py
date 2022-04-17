class Solution(object):
    def nextPermutation(self, nums):

        i = len(nums) -2

        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) -1
            while nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]
            self.reverse(nums, i+1)
        return nums

    def reverse(self, nums, start):
        end = len(nums) -1
        i = start

        while i < end:
            nums[i], nums[end] = nums[end], nums[i]
            i += 1
            end -= 1

