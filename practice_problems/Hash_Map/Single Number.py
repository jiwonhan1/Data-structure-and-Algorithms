from collections import defaultdict
class Solution:
    # Time and space complexity O(N)
    def singleNumber(self, nums):
        numDict = {}

        for num in nums:
            numDict[num] = 1 if num not in numDict else numDict[num] + 1

        for num in numDict:
            if numDict[num] == 1:
                return num

    def singleNumber2(self, nums):
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i