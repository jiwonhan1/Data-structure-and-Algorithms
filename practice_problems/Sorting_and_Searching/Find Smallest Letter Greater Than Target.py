class Solution:
    # Time complexity O(N)
    # Space complexity O(1)
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]