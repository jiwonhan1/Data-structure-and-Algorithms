class Solution(object):
    def isAnagram(self, s,t):
        if len(s) != len(t):
            return False
        str1 = list(s)
        str2 = list(t)

        return sorted(str1) == sorted(str2)

    def isAnagram2(self, s, t):
        if len(s) != len(t):
            return False

        char = [0] * 26
        for i in range(len(s)):
            char[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            char[ord(t[i]) - t[i]] -= 1
            if char[ord(t[i]) - ord('a')] < 0:
                return False
        return True