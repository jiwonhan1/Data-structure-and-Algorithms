class Solution:
    # Time complexity O(maxK * N)
    def decodeString(self,s):
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                decodedString = []
                while stack[-1] != '[':
                    decodedString.append(stack.pop())
                # remove [
                stack.pop()
                base = 1
                k = 0

                while stack and stack[-1].isdigit():
                    k = k + int(stack.pop()) * base
                    base *= 10

                while k != 0:
                    for j in range(len(decodedString)-1,-1,-1):
                        stack.append(decodedString[j])
            else:
                stack.append(s[i])
        return ''.join(stack)