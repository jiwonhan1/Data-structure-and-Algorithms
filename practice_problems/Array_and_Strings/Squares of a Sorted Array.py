class Solution(object):
    # Sort
    # Time complexity O(NlogN) Space complexity O(N)
    def sortedSquares(self, nums):
        return sorted(x*x for x in nums)

    # Two Pointers
    # Time complexity O(N) Space complexity O(N)
    def sortedSquares2(self, nums):
        n = len(nums)

        result = [0] * n

        left = 0
        right = n - 1
        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result

    def sortedSquares2(self, nums):
        n = len(nums)
        result = [0] * n
