class Solution(object):
    def findNumbers(self, nums):
        result = 0
        for num in nums:
            if 9 < num < 100 or 999 < num < 10000 or num == 100000:
                result += 1
        return result