class Solution:
    def repeatedSubstringPattern(self, s):
        if len(s) < 1:
            return False
        if len(s) == 2:
            if s[0] != s[1]:
                return False
            else:
                return True

        for i in range(1,len(s)):
            if len(s) % i == 0:
                if s[:i] * int(len(s) / i) == s:
                    return True
        return False