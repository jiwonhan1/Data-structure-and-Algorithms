class Solution:
    # Time and Space complexity O(N)
    def simplifyPath(self, path):
        stack = []
        for portion in path.split('/'):
            # '..' refers to the directory up a level
            if portion == '..':
                if stack:
                    stack.pop()
            elif portion == '.' or not portion:
                continue
            else:
                stack.append(portion)
        final_str = '/' + '/'.join(stack)
        return final_str