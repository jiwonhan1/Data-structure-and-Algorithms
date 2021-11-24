class Solution(object):
    # Time complexity O(logN) Space complexity O(1)
    def mySqrt(self, x):
        if x < 2:
            return x
        # Set the left boundary to 2, and the right boundary to x / 2
        left, right = 0, x // 2

        while left <= right:
            # Take num = (left + right) / 2 as a guess
            # Compute num * num and compare it with x
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right