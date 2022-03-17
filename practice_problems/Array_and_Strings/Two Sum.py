class Solution(object):
    # Brute Force
    # Loop through each element x and find if there is another value that equals to target -x
    # Time complexity O(N2) space complexity O(1)
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
    # One-pass Hash Table
    # To improve our runtime complexity, we need a more efficient way to check if the complement exists in the array
    # If the complement exists, we need to get its index
    #  What is the best way to maintain a mapping of each element in the array to its index? A hash table
    # We can reduce the lookup time from O(n) to O(1) by trading space for speed
    # A hash table is well suited for this purpose because it supports fast lookup in near contant time
    # I say "near" because a collision occured, a lookup could degenerate to O(n) time
    # However, lookup in a hash table should be amortized O(1) time as long as the hash function was chosen carefully
    # Time complexity O(n) Space complexity O(n)
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [i,map[complement]]
            map[nums[i]] = i