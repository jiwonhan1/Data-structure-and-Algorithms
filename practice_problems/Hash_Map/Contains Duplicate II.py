class Solution:
    def containsNearbyDuplicate(self, nums, k):
        numSet = set()

        for i in range(len(nums)):
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
            if len(numSet) > k:
                numSet.remove(nums[i])
        return False