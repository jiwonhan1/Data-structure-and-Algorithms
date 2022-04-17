import unittest
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        p1 = 0
        p2 = 0

        for p in range(n+m):
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
        return nums1
class TestMergeSortedArray(unittest.TestCase):
    def test_merge_sorted_array(self):
        actual = Solution.merge(self,[1,2,3,0,0,0], 3, [2,5,6], 3)
        expected = [1,2,2,3,5,6]
        self.assertEqual(actual, expected)