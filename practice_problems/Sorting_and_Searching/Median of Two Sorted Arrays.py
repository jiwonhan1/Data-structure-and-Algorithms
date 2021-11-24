class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        newArray = nums1 + nums2
        newArray.sort()

        if len(newArray) % 2 == 0:
            return float(newArray[len(newArray) // 2] + newArray[len(newArray) // 2 -1]) / 2
        else:
            return float(newArray[len(newArray) // 2])
