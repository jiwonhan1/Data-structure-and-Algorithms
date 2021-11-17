class Solution(object):
    # Three Pointers (Start from the begining)
    # Time complexity O(N+M)
    # Space complexity O(M)
    # Initialize nums1Copy to be a new array containing the first m values of nums1
    # Initialize read pointer p1 to the beginning of nums1Copy
    # Initialize read pointer p2 to the beginning of nums2

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