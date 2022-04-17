from collections import deque
class Solution:
    # Time and Space complexity O(N)
    def depthSum(self, nestedList):
        def dfs(nested_list, depth):
            total = 0
            for nested in nested_list:
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    total += dfs(nested.getList(), depth + 1)
            return total
        return dfs(nestedList, 1)

    def depthSum(self, nestedList):
        queue = deque(nestedList)
        depth = 1
        total = 0

        while queue:
            for i in range(len(queue)):
                nested = queue.pop()
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    queue.extendleft(nestedList.getList())
            depth += 1
        return total