class Solution(object):
    # Time complexity: O(n ^ 2)
    def singleNumber(self, nums):
        no_duplicate_nums = []
        for num in nums:
            if num not in no_duplicate_nums:
                no_duplicate_nums.append(num)
            else:
                no_duplicate_nums.remove(num)
        return no_duplicate_nums.pop()

    # Time complexity O(n)
    def singleNumber2(self, nums):
        hash_table = {}

        for num in nums:
            hash_table[num] += 1
        for num in nums:
            if hash_table[num] == 1:
                return num