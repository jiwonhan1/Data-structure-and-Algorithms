class Solution(object):
    # Time complexity O(n)
    # Space complexity O(1)
    def reverseString(self,s):
        left, right = 0, len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return s
    # Time complexity O(N)
    # Space complexity O(N)
    def reverseString2(self,s):
        def helper(left,right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right-1)
        helper(0, len(s)-1)