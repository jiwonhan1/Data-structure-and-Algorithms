class Solution(object):
    # Time complexity O(log N) Space complexity O(1)
    def findMin(self, nums):
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]
        # left pointer
        left = 0
        # right pointer
        right = len(nums) -1

        # if the last element is greater than the first element then there is no rotation
        if nums[right] > right[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) // 2
            # If the mid element is greater than its next element then mid+1 element is the smallest
            if nums[mid + 1] < nums[mid]:
                return nums[mid+1]
           # If the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid] < nums[mid -1]:
                return nums[mid]
            # if the mid elements value is greater than the 0th element this means the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] < nums[0]:
                left = mid + 1
            else:
                right = mid - 1

