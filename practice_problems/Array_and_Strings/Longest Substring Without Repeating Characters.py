class Solution(object):
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