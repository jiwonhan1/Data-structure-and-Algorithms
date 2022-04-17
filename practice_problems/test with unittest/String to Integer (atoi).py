import unittest
class Solution(object):
    def myAtoi(self, s):

        index = 0
        n = len(s)

        while index < n and s[index] == ' ':
            index += 1

        sign = 1
        if index < n and s[index] == '+':
            index += 1
        elif index < n and s[index] == '-':
            index += 1
            sign = -1

        result = 0
        while index < n and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        if result * sign > 2 ** 31 -1:
            return 2 ** 31 -1
        elif result * sign < -2 ** 31:
            return -2 ** 31
        else:
            return result * sign

class TestStringAtoi(unittest.TestCase):
    def test_string_atoi(self):
        actual = Solution.myAtoi(self, '  -42')
        expected = -42
        self.assertEqual(actual, expected)
