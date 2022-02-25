class Solution(object):
    # Time complexity O(n)
    def myAtoi(self,s):
        if s == "":
            return 0

        s = s.strip()
        neg = 1

        if s and s[0] == '-':
            neg = -1
            s = s[1:]
        elif s and s[0] == '+':
            s = s[1:]

        num = 0

        for c in s:
            if c.isdigit():
                num = (num * 10) + int(c)
            else:
                break
        res = num * neg

        if res >= 2** 31:
            return 2**31 -1
        elif res < -2 ** 31:
            return -2 ** 31
        return res
    def myAtoi(self, s):
        sign = 1
        result = 0
        index = 0
        n = len(s)

        INT_MAX = 2 ** 31 -1
        INT_MIN = -2 ** 31

        while index < n and s[index] == ' ':
            index += 1

        if index < n and s[index] == '+':
            index += 1
        elif index < n and s[index] == '-':
            index += 1
            sign = -1

        while index < n and s[index].isdigit():
            digit = int(s[index])
            result = 10 * result + digit
            index += 1

        if result:
            if result * sign > INT_MAX:
                return INT_MAX
            elif result * sign < INT_MIN:
                return INT_MIN
            else:
                return result * sign
        else:
            return 0