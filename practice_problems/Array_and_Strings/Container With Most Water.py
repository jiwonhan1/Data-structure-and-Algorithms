class Solution(object):
    # Two pointer approach
    # Time complexity O(n) space complexity O(1)
    # We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines.
    # Further, we maintain a variable maxarea to store the maximum area obtained till now.
    # At every step, we find out the area formed between them, update maxarea and move the pointer pointing to the shorter line towards the other end by one step.
    def maxArea(self, height):
        maxarea = 0
        l = 0
        r = len(height) -1
        while l < r:
            maxarea = max(maxarea, min(height[l], height[r])- (r -l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea