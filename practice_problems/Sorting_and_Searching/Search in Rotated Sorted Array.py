class Solution(object):
    # Time complexity O(log N) Space complexity O(1)
    def search(self, nums, target):
        start, end = 0, len(nums) -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    mid = end - 1
                else:
                    mid = start + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1