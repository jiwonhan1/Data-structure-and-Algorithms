class Solution(object):
    # Time complexity O(N) Space complexity O(1)
    def twoSum(self, numbers, target):
        low = 0
        high = len(numbers) -1
        while low < high:
            num = numbers[low] + numbers[high]
            if num == target:
                return [low+1, high+1]
            elif num < target:
                low += 1
            else:
                high -= 1
        return [-1,-1]