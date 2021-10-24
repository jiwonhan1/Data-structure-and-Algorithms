class Solution(object):
    def maxArea(self, height):
        maxarea = 0
        l = 0
        r = len(height) -1
        while l < r:
            maxarea = max(maxarea, min(height[l], height[r])- (r -l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxarea