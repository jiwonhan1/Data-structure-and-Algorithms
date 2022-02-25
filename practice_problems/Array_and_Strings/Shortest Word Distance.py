class Solution(object):
    # Time complexity: O(N⋅M)
    # Space complexity O(1)
    def shortestDistance(self, wordsDict, word1, word2):
        i1 = -1
        i2 = -1

        minDistance = len(wordsDict)

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                i1 = i
            if wordsDict[i] == word2:
                i2 = i
            if i1 != -1 and i2 != -2:
                minDistance = min(minDistance, abs(i2-i1))

        return minDistance
