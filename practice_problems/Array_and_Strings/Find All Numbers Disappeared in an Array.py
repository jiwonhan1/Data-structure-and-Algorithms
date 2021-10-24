class Solution(object):
    # Time complexity O(N)
    def findDisappearedNumbers(self, nums):
        hash_table = {}

        for num in nums:
            hash_table[num] = 1

        result = []

        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)

        return result