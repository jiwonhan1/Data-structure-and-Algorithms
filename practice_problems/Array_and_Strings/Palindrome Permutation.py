class Solution(object):
    def canPermutePalindrome(self,s):
        unpaired_chars = set()

        for c in s:
            if c not in unpaired_chars:
                unpaired_chars.add(c)
            else:
                unpaired_chars.remove(c)
        return len(unpaired_chars) <= 1

