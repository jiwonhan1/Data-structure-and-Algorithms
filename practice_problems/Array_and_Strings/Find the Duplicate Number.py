class Solution(object):
    # Time complexity O(nlogn)
    # Space complexity O(logn) or O(n)
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    # Time complexity O(n)
    # Space complexity O(n)
    def findDuplicate2(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

    # Time complexity O(nlogn)
    # Space complexity O(1)
    def findDuplicate3(self, nums):
        low = 1
        high = len(nums) -1

        while low <= high:
            cur = (low + high) // 2
            count = 0

            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
        return duplicate
