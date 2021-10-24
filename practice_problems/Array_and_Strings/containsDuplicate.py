class Solution(object):
    # Time complexity : O(n) Space complexity : O(n)
    def containsDuplicates(self, nums):
        validNums = set()
        for i in range(len(nums)):
            if nums[i] in validNums:
                return True
            validNums.add(nums[i])
        return False

    # Time complexity : O(nlogn) Space complexity : O(1)
    def containsDuplicates2(self, nums):
        nums.sort()
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                return True
        return False

