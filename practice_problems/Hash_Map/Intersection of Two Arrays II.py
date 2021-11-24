from collections import defaultdict
class Solution:
    # Time and space complexity O(N+M)
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        hashmap = defaultdict(int)

        for n in nums1:
            hashmap[n] += 1

        res = []
        for n in nums2:
            if n in hashmap and hashmap[n] > 0:
                res.append(n)
                hashmap[n] -= 1
        return res