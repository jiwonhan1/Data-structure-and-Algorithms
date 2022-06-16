from functools import cache
class Solution(object):
    # Memoization1
    # Time and space complexity O(MN)
    # there are M N subproblems
    def longestCommonSubsequence(self, text1, text2):
        @cache
        def memo_solve(p1, p2):
            # Base case: If either string is now empty, we can't match
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Recursive case 1.
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1+1, p2+1)
            else:
                return max(memo_solve(p1, p2+1), memo_solve(p1+1, p2))
        return memo_solve(0,0)

    # Dynamic Programming with 2D Array
    def longestCommonSubsequence(self, text1, text2):
        dp_grid = [[0] * (len(text2)+1) for _ in (len(text2)+1)]
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1+ dp_grid[row+1][col+1]
                else:
                    dp_grid[row][col] = max(dp_grid[row+1][col], dp_grid[row][col+1])
            return dp_grid[0][0]