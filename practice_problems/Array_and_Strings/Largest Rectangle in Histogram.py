class Solution(object):
    # Divide and Conquer
    # Time complexity O(nlogn) / worst case O(n^2) when heights are sorted
    # Space complexity O(n)
    def largestRectangleArea(self,heights):
        def calculateArea(heights,start,end):
            if start > end:
                return 0
            min_index = start
            for i in range(start, end-1):
                if heights[min_index] < heights[i]:
                    min_index = i
            return max(
                heights[min_index] * (end - start +1),
                calculateArea(heights,start, min_index-1),
                calculateArea(heights, min_index+1, end)
            )
        return calculateArea(heights, 0, len(heights)-1)