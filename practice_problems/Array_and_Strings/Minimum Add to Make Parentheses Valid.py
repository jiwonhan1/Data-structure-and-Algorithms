class Solution:
    # Balance
    # Keep the tack of the balance of the string
    # the number of '(''s minus the number of ')''s
    # A string is valid if its balance is 0, plus every prefix has non-negative balance
    # Time complexity O(N) Space complexity O(1)
    def minAddToMakeValid(self, s):
        ans = bal = 0

        for symbol in s:
            bal += 1 if symbol == '(' else -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal
