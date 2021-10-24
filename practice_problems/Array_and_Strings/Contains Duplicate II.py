class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashmap = {}
        for index, value in enumerate(nums):
            if value in hashmap and index - hashmap[value] <= k:
                return True
            hashmap[value] = index
        return False