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