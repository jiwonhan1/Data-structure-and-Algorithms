class Solution:
    # Brute Force
    # Time complexity O(n^2 * k)
    # Space complexity O(n^2)
    def palindromePairs(self,words):
        pairs = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                combined_word = word1 + word2
                if combined_word == combined_word[::-1]:
                    pairs.append([i,j])
        return pairs