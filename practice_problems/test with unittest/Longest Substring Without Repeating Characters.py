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
    def lengthOfLogestSubstring2(self,s):
        def check(start,end):
            chars = [0] * 128
            for i in range(start, end+1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True

        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i,j):
                    res = max(res, j-i+1)
        return res

class TestLengthOfLongestSubstring(unittest.TestCase):
    def test_length_of_longest_substring(self):
        actual = Solution.lengthOfLongestSubstring(self,"abcabcbb")
        expected = 3
        self.assertEqual(actual, expected)
    def test_length_of_longest_substring2(self):
        actual = Solution.lengthOfLogestSubstring2(self, "abcabcbb")
        expected =3
        self.assertEqual(actual, expected)