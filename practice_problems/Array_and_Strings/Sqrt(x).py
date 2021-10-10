class Solution(object):
    # Time complexity O(logN) Space complexity O(1)
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 0, x // 22

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right