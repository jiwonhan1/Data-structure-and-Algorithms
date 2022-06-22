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

    # Memoization2
    # Time complexity O(MN2)
    # Space complexity O(MN)
    def longestCommonSubsequence(self, text1, text2):
        @cache(maxsize=None)
        def memo_solve(p1, p2):
            # Base case: If either string is now empty, we can't up anymore characters
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Option 1: We don't include text[p1] in the solution.
            option_1 = memo_solve(p1+1, p2)

            # Option 2: We include text1[p1] in the solution, as long as a match for it in text2 at or after p2 exists
            first_occurnece = text2.find(text1[p1], p2)
            option_2 = 0
            if first_occurnece != -1:
                option_2 = 1 + memo_solve(p1+1, first_occurnece+1)

            return max(option_1, option_2)

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