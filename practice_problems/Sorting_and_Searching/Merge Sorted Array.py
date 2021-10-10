class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]

        p1 = 0
        p2 = 0

        for i in range(n+m):
            if p2 >= n or (p1 < n and nums1_copy[p1] <= nums2[n]):
                nums1[i] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1