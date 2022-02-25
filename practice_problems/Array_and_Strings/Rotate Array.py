class Solution:
    # Brute Force
    # Time complexity O(nk)
    # Space complexity O(1)
    def rotate(self, nums, k):
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], nums[previous] = nums[previous], nums[j]

    # Using Reverse
    # Time complexity O(N)
    # Space complexity O(1)
    # This approach is based on the fact that when we roate the array k times, k elements from the back end fo the array come to the front and the rest of the elements from the front shift backwards.
    # In this approach, we firstly reverse all the elements of the array
    # Then, reversing the first k elements followed by reversing the rest n-k elements gives us the required result.
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
