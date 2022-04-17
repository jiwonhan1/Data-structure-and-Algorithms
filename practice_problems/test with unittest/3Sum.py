import unittest
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums,i,res)
        return res
    def twoSum(self,nums,i,res):
        lo, hi = i+1, len(nums) -1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo-1] == nums[lo]:
                    lo += 1
    def threeSum2(self, nums):
        res, dups = set(), set()
        seen = {}

        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 -val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted([val1, val2, complement])))
                    seen[val2] = i
        return res
class Test3Sum(unittest.TestCase):
    def test_3_sum(self):
        actual = Solution.threeSum2(self,[-1,0,1,2,-1,-4])
        expected = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(actual, expected)