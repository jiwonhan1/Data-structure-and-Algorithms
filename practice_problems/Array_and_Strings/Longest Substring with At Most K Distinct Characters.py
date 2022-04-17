from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistanct(self, s,k):
        n = len(s)

        if n * k == 0:
            return 0
        left, right = 0, 0
        hashmap = defaultdict()

        max_len = 1

        while right < n:
            hashmap[s[right]] = right
            right += 1
            if len(hashmap) == k+1:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                left = del_idx + 1
            max_len = max(max_len, right - left)
        return max_len