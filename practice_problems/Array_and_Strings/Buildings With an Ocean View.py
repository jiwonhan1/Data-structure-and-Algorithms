class Solution:
    # Time complexity O(N)
    # Space complexity O(N)
    def findBuildings(self, heights):
        n = len(heights)
        answer = []

        for current in range(n):
            while answer and heights[answer[-1]] <= heights[current]:
                answer.pop()
            answer.append(current)
        return answer