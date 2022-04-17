class Solution(object):
    def moveZeros(self, nums):
        i = 0
        j = 0

        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1