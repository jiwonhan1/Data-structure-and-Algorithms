class Solution:
    # Brute Force
    # Time complexity O(n^2 * k)
    # Let n be the number of words, and k be the length of the longest word
    # There are n2 pairs of words. Then appending 2 words requires time 2k,
    # as does reversing it and then comparing it for equality.
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