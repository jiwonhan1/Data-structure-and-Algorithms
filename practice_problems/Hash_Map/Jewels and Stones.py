class Solution:
    # Time complexity O(J + S)
    # Space complexity O(J)
    def numJewelsStones(self, jewels, stones):
        Jset = set(jewels)
        return sum(s in Jset for s in stones)