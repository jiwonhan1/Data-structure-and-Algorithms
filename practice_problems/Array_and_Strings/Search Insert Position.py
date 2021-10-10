class Solution(object):
    # Time complexity O(logN)
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) -1
        while left <= right:
            pivot = (left+right) // 2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] > target:
                left = pivot + 1
            else:
                right = pivot -1
        return left