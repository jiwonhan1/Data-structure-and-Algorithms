class Solution(object):
    # Sort
    # Time complexity O(N log N)
    # Space complexity O(N)
    def sortArrayByParity(self, nums):
        nums.sort(key = lambda x:x%2)
        return nums

    # Two Pass
    # Time complexity O(N)
    # Space complexity O(N)
    def sortArrayByParity(self, nums):
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]


    # In-Place
    # Time complexity O(N)
    # Space complexity O(1)
    def sortArrayByParity(self, nums):
        i, j = 0, len(nums)-1

        while i < j:
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] % 2 == 0: i += 1
            if nums[j] % 2 == 1: j -= 1
        return nums