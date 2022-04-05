class Solution(object):
    # Using two pointers
    # Time complexity O(n) Space complexity O(n)
    # If there is a larger bar at one end, we are assured that the water trapped would be dependent on height of bar in current direction.
    # As soon as bar at other end is smaller, we start iterating in opposite direction.
    # We must maintain left_max and right_max during the iteration, but now we can do it one iteration using 2 pointers, switching between the two.
    def trap(self, height):
        if len(height) == 0:
            return 0
        left = 0
        right = len(height)-1
        leftMax = rightMax = 0

        ans = 0

        while left < right:
            if height[left] > leftMax:
                leftMax = height[left]
            if height[right] > rightMax:
                rightMax = height[right]
            if height[left] < height[right]:
                ans += max(0, leftMax - height[left])
                left += 1
            else:
                ans += max(0, rightMax - height[right])
                right -= 1

        return ans

    # Dynamic Programming
    # Space/Time complexity O(N)
    # Find the maximum height of bar from the left and end upto an index i in the array left_max
    # Find maximum height of bar from the right end upto an index i in the array right_max
    # Iterate over the height array and update ans:
    # Add min(left_max[i], right_max[i]) - height[i] to ans
    def trap(self, height):

        N = len(height)
        if N < 3: return 0

        result = 0
        l_max, r_max = [0] * N, [0] * N
        l_max[0] = height[0]

        for i in range(1, N):
            l_max = max(height[i], l_max[i-1])

        r_max[N-1] = height[N-1]

        for j in range(N-2, -1,-1):
            r_max = max(height[i], r_max[i+1])

        for i in range(1, N-1):
            result += min(l_max[i], r_max[i]) - height[i]

        return result

    # def trapStack(self, height):
    #     result, i = 0, 0
    #
    #     stack = []
    #
    #     while i < len(height):
    #         while stack and height[stack[-1]] < height[i]:
    #             t = stack.pop()
    #             if not stack: break
    #             dist = i - st[-1] -1