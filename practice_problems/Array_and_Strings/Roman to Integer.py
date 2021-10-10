class Solution(object):
    def romanToInt(self, s):
        romanInt = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        i = result = 0

        while i < len(s):
            if i+1 < len(s) and s[i] < s[i+1]:
                result += romanInt[s[i+1]] - romanInt[s[i]]
                i += 2
            else:
                result += romanInt[s[i]]
                i += 1
        return result