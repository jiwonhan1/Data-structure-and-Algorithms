import unittest
class Solution(object):
    def lengthOfLongestSubstring(self,s):
        chars = [0] * 128

        left= right = 0
        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
            res = max(res, right - left +1)
            right += 1
        return res
class TestLengthOfLongestSubstring(unittest.TestCase):
    def test_length_of_longest_substring(self):
        actual = Solution.lengthOfLongestSubstring(self,"abcabcbb")
        expected = 3
        self.assertEqual(actual, expected)