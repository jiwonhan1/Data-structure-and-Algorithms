class Solution:
    def intersection(self, nums1, nums2):
        result = []
        d = {}
        for i in nums1:
            d[i] = 1 if i not in d else d[i]+1

        for n in nums2:
            if n in d:
                result.append(n)
                d[n] -= 1
        return result