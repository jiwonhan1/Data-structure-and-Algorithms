class Solution(object):
    # Time complexity O(log N) Space complexity O(1)
    def searchRange(self, nums, target):
        lower_bound = self.findBound(nums, target, True)
        upper_bound = self.findBound(nums, target, False)

        return [lower_bound, upper_bound]

    def findBound(self, nums, target, isFirst):
        N = len(nums)
        begin, end = 0, N -1

        while begin <= end:
            mid = begin+end / 2
            if nums[mid] == target:
                if isFirst:
                    if mid == target or nums[mid -1] < target:
                        return mid
                    end = mid - 1
                else:
                    if mid == target or nums[mid+1] > target:
                        return mid
                    begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return - 1
