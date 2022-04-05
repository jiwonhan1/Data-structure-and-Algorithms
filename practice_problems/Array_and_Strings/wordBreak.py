class Solution:
    # Brute Force
    # Time complexity O(2n)
    # Given a string of length n, there are n+1 ways to split it into two parts
    # At each step, we have a choice, to split or not split. In the worse case, when all choices are to be checked, that results in O(2n)
    # Space complexity O(N)
    def wordBreak(self, s, wordDict):
        def wordBreakRecur(s, word_dict, start):
            if start == len(s):
                return True

            for end in range(start+1, len(s)+1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    return True
                return False
        return wordBreakRecur(s, set(wordDict), 0)
