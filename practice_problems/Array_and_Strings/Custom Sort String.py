from collections import Counter
class Solution:
    # Count and Write
    # Time complexity O(order.length + s.length)
    # Space complexity O(s.length)
    def customSortString(self, order, s):
        count = Counter(s)
        ans = []

        for c in order:
            ans.append(c * count[c])
            count[c] = 0

        for c in count:
            ans.append(c * count[c])
        return ''.join(ans)