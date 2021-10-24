class Solution(object):
    def reverse(self,x):
        INT_MAX = 2 ** 31 -1
        remainder = abs(x)
        result = 0

        while remainder:
            remainder, digit = divmod(remainder, 10)
            result = digit + (result * 10)
        if x < 0:
            result = - result
        if result > INT_MAX:
            return 0
        elif result < -INT_MAX:
            return 0
        return 0
