class Solution:
    # Using a stack and String Builder
    # Time complexity O(N) Space complexity O(N)
    def minRemoveToMakeValid(self, s):

        stack = []

        indexes_to_remove = set()

        for i,c in enumerate(s):
            if c not in '()':
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack))

        stringbuilder = []

        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                stringbuilder.append(c)
        return ''.join(stringbuilder)