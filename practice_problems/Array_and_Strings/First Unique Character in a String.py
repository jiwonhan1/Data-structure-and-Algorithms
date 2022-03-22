from collections import Counter
class Solution(object):
    # Hash Map
    # Time complextiy O(N) Space complextiy O(1) because English alphabet contains 26 letters
    def firstUniqChar(self,s):
        count = Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1

    # Fixed Array with ascii code
    # Time complexity O(N)
    # Space complexity O(1)
    def firstUniqChar(self,s):
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i].lower()) - ord('a')] += 1

        for i in range(len(s)):
            if count[ord(s[i].lower()) - ord('a')] == 1:
                return i

        return -1