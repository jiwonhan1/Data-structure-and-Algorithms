class Solution:
    # Time and space complexity O(N)
    def containsDuplicate(self, nums):
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
        return False