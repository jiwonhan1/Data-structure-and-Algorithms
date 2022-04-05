class Solution:
    # Single Scan
    # We can traverse over all the elements of the flowerbed and find out those elements
    # which are 0 (implying an empty position).
    # For every such element, we check if its both adjacent positions are also empty
    # If so, we can plan a flower at the current position
    # without violating the no-adjacent-flowers-rule
    # For the first and last elements, we need not check the previous and the next adjacent positions repectively
    # Time complexity O(N) Space complexity O(1)
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left_plot = (i==0) or (flowerbed[i-1] == 0)
                empty_right_plot = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    count += 1
        return count >= n