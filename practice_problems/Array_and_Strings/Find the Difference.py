from collections import Counter

class Solution(object):
    # Time Complexity: O(Nlog(N))
    def findDifference(self, s, t):
        sorted_s = s.sort()
        sorted_t = t.sort()

        i = 0

        while i < len(s):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]
            i += 1
        return sorted_t[i]
    # Time Complexity O(N)
    def findDifference2(self, s, t):
        counter_s = Counter(s)
        for ch in t:
            if ch not in counter_s and counter_s[ch] == 0:
                return ch
            else:
                counter_s[ch] -= 1