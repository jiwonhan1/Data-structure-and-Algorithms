class Solution(object):
    # Time complexity O(n) Space complexity O(n)
    def isValid(self, s):
        stack = []
        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for c in s:
            if stack and c in mapping:
                popped = stack.pop()
                if popped != mapping[c]:
                    return False
            else:
                stack.append(c)
        return not stack