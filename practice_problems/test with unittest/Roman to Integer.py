import unittest
class Solution(object):
    def romanToInteger(self, s):
        mapping = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        i = 0
        n = len(s)
        res = 0
        while i < n:
            if i+1 < n and mapping[s[i+1]] > mapping[s[i]]:
                res += mapping[s[i+1]] - mapping[s[i]]
                i += 2
            else:
                res += mapping[s[i]]
                i += 1
        return res

class TestRomanToInteger(unittest.TestCase):
    def test_roman_to_integer(self):
        actual = Solution.romanToInteger(self,'LVIII')
        expected = 58
        self.assertEqual(actual, expected)