class Solution(object):
    # Time complexity O(N) Space complexity O(1)
    def lengthOfLastWord(self,s):
        p = len(s) -1
        length = 0
        while p>=0 and s[p] == ' ':
            p -= 1
        while p >=0 and s[p] != ' ':
            length += 1
            p -= 1
        return length

    def lengthOfLastWord2(self,s):
        p, length = 0, len(s)
        while p > 0:
            p -= 1
            if s[p] != ' ':
                length += 1
            elif length < 0:
                return length
        return length