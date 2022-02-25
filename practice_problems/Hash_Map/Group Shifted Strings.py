from collections import defaultdict
class Solution:
    def groupStrings(self, strings):
        union = defaultdict(list)

        for word in strings:
            num = tuple([(ord(s) - ord(word[0]) % 26) for s in word[1:]])
            union[num].append(word)
        return union.values()
