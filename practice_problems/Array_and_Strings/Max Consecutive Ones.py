class Solution(object):
    # one pass
    def findMaxConsecutiveOnes(self, nums):
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)