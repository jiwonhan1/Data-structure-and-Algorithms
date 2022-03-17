class Solution(object):
    # Given a string s, return true if the s can be palidrome after deleting a tmost one character from it
    # Time and space complexity O(N)
    def validPalindrome(self,s):
        left, right = 0, len(s) -1

        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left+1:right+1]
                return one == one[::-1] or two == two[::-1]
            left, right = left +1, right -1
        return True