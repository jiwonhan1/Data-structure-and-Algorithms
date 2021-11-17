class Solution:
    # One Pass
    # Time complexity O(N) / in-place
    def sortColor(self, nums):
        p0 = curr = 0
        p2 = len(nums) -1

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

