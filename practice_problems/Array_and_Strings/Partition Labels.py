class Solution(object):
    # Greedy
    # Time complextiy O(N)
    # Space complexity O(1)
    def partitionLabels(self,s):
        last = {c:i for i, c in enumerate(s)}

        j = anchor = 0
        ans = []

        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                ans.append(i-anchor +1)
                anchor = i + 1