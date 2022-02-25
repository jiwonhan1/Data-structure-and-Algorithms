class Solution(object):
    # Two Pointers
    # Time complexity O(N)
    # Space complexity O(1)
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+= 1
        return i

    # Two Pointers2
    # Time complexity O(N)
    # Space complexity O(1)
    def removeElement(self, nums, val):
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n