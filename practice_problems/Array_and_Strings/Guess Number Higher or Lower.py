## guess API

class Solution:
    def guessNumber(self, n):
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                low = mid + 1
            else:
                high = mid -1
        return -1