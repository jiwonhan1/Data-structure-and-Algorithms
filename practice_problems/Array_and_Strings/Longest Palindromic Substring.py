class Solution(object):
    def longestPalindrome(self,s):
        m = ''
        # Time complexity O(N4)
        # Two for-loops and slicing operation and reverse string
        for i in range(len(s)):
            for j in range(len(s), i , -1):
                if len(m) > j-i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m