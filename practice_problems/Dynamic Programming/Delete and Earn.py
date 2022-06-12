from collections import defaultdict
class Solution(object):

    # Bottom-Up Dynamic Programming
    # Time complexity O(N+k)
    # Space complexity O(N+k)
    def deleteAndEarn(self, nums):
        points = defaultdict(int)
        max_number = 0

        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        max_points = [0] * (max_number+1)

        max_points[1] = points[1]

        for num in range(2, len(max_points)):
            max_points[num] = max(max_points[num-1], max_points[num-2] + points[num])
        return max_points[max_number]