from collections import defaultdict
import operator

class Solution(object):
    def mostCommonWord(self, paragragh, banned):
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragragh])

        words = normalized_str.split()

        word_count = defaultdict(int)
        banned_words = set(banned)

        for w in words:
            if w not in banned_words:
                word_count[w] += 1
        return max(word_count.items(), key=operator.itemgetter(1))[0]