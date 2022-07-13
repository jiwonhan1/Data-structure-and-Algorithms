from functools import lru_cache
class Solution:
    # Brute Force
    # The naive approach to solve this problem is to use recursion and backtracking.
    # For finding the solution, we check every possible prefix of that string in the dictionary of words,
    # if it is found in the dictionary, then the recursive function is called for the remaining portion of that string.
    # And, if in some function call it is found that the complete string is in dictionary, then it will return true
    # Time complexity O(2n). Given a string of length n, there are n+1 ways to split i into two parts
    # At each step, we have a choice: to split or not to split.
    # In the worse case, when all choices are to be checked, that results in O(2n)
    # Space complexity O(n)
    def wordBreak(self, s, wordDict):
        def wordBreakRecur(s, word_dict, start):
            if start == len(s):
                return True

            for end in range(start+1, len(s)+1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    return True
            return False
        return wordBreakRecur(s, set(wordDict), 0)

    # Recursion with memoization
    # When the function is called again for a particular string, value will be fetched and returned using the memo array,
    # if its value has been already evaluated.
    # With memoization many redundant subproblems are avoided and recursion tree is pruned and thus it reduces the time complexity by a large factor
    def wordBreak(self, s, wordDict):
        @lru_cache
        def wordBreakMemo(s, word_dict, start):
            if start == len(s):
                return True
            for end in range(start+1, len(s)+1):
                if s[start:end] in word_dict and wordBreakMemo(s, word_dict, end):
                    return True
            return False
        return wordBreakMemo(s, frozenset(wordDict), 0)

    # Using Dynamic Programming
    # Time complexity O(n3)
    # There are two nested loops, and substring computation at each iteration
    # Space complexity O(n)
    def wordBreak(self,s, wordDict):
        word_set = set(wordDict)
        dp = [False] * (len(s) +1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]
