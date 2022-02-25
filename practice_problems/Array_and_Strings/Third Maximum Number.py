import heapq

class Solution(object):
    # Use a Set and Delete Maximum
    # Time complexity O(N)
    # Space complexity O(N)
    def thirdMax(self, nums):
        nums= set(nums)
        maximum = max(nums)
        if len(nums) < 3:
            return maximum
        nums.remove(maximum)
        second_maximum = max(nums)
        nums.remove(second_maximum)
        return max(nums)

    # Keep Track of 3 Maximums Using a Set
    # Time complexity O(N)
    # Space Complexity O(1) since maximums never holds more than 3 items at a time. 
    def thirdMax(self, nums):
        maximums = set()
        for num in nums:
            maximums.add(num)
            if len(maximums) > 3:
                maximums.remove(min(maximums))
        if len(maximums) == 3:
            return min(maximums)
        return max(maximums)

    # Using heapq
    def thirdMax(self, nums):
        min_heap = []
        for num in nums:
            if num in min_heap:
                continue
            if len(min_heap) < 3:
                heapq.heappush(min_heap, num)
            elif len(min_heap) == 3:
                heapq.heappushpop(min_heap, num)
