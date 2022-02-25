class Solution(object):
    # Backtracking
    # Time complexity O(4^n * N)
    # Space complexity O(N)
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        letters = {"2":"abc", "3": "def", "4":"ghi",
                  "5": "jkl", "6": "mno", "7":"pqrs",
                   "8": "tuv", "9":"wxyz"}
        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append(''.join(path))
                return
            possible_letters = letters[digits[index]]

            for letter in possible_letters:
                path.append(letter)
                backtrack(index+1,path)
                path.pop()
        combinations = []
        backtrack(0,[])
        return combinations