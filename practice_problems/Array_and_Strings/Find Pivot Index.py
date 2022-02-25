class Solution:
    # We need to quickly compute the sum of values to the left and the right of every index.
    # Let's say we knew S as the sum of the numbers, and we are at index i.
    # If we knew the sum of numbers leftsum that are to the left of index i, then the other sum to the right of the index would just be S-nums[i]-leftsum.
    # Time complexity O(N) Space complexity O(1)
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S-leftsum-x):
                return i
            leftsum += x
        return -1