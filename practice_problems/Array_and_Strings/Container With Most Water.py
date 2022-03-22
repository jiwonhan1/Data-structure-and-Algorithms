class Solution(object):
    # Brute Force
    # We will simply consider the area for every possible pair of the lines and find out the maximum area out of those.
    # Time complexity O(N) Space complexity O(1)
    def maxArea(self, height):
        maxarea = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                maxarea = max(maxarea, min(height[i], height[j])* j-i)

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