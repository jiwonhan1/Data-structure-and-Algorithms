import unittest
class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)

        L,R,answer = [0] *length, [0]*length,[0] *length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i-1] * L[i-1]

        R[length-1] = 1
        for i in range(length-2, -1,-1):
            R[i] = R[i+1] * nums[i+1]

        for i in range(length):
            answer[i] = R[i] * L[i]

        return answer

class TestProductExceptSelf(unittest.TestCase):
    def test_product_except_self(self):
        actual = Solution.productExceptSelf(self,[1,2,3,4])
        expected = [24,12,8,6]
        self.assertEqual(actual, expected)