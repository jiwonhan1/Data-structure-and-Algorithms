import collections


class Solution(object):
    # Time complexity O(NKlogK) Space complexity O(NK)
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs: # Time complexity O(N)
            ans[tuple(sorted(s))].append(s) # Time complexity (K log K)
        return ans.values()

    # Time complexity O(NK) and Space complexity O(NK)
    def groupAnagrams2(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
