class Solution(object):

    # Brute Force
    # Check all the substring one by one to see if it has no duplicate character
    # Time complexity O(N3)
    # Space complexity O(min(n,m))
    def lengthOfLongestSubstring(self, s):
        def check(start,end):
            chars = [0] * 26
            for i in range(start, end+1):
                c = s[i]
                chars[ord[c] - ord['a']] += 1
                if chars[ord[c]] > 1:
                    return False
            return True

        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j-i+1)
        return res

    # Sliding Window
    # A sliding window is an abstract concept commonly used in array/string problems
    # A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i,j]
    # A sliding window is a window 'slides' its two boundaries to the certain direction
    # For example, if we slide [i,j) to the right by 1 element, then it becomes [i+1, j+1)
    # We use hashSet to store the characters in current window.
    # Then we slide the index j to the right. If it is not in the HashSet, we slide j further.
    # Doing so until s[j] is already in the HashSet
    # Time complextiy O(2n) = O(n)
    # Space complexity O(min(m,n))

    def lengthOfLongestSubstring(self,s):
        # By using HashSet as a sliding window, checking if a character in the current can be done in O(1)
        chars = [0] * 128
        left = right = 0

        res = 0

        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left +=1
            res = max(res, right - left +1)
            right += 1
        return res