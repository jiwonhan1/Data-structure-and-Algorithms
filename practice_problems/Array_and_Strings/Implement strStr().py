class Solution(object):
    def strStr(self, haystack, needle):
        n, l = len(haystack), len(needle)
        for i in range(n - l + 1):
            if haystack[i:i+l] == needle:
                return i
        return -1
