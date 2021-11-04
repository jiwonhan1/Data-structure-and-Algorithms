from collections import Counter
class Solution(object):
    # Time complextiy O(N) Space complextiy O(1) because English alphabet contains 26 letters
    def firstUniqChar(self,s):
        count = Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1