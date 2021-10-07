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