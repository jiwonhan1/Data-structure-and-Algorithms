class Solution(object):
    def parseTernary(self, expression):
        stack = []
        for i in range(len(expression)-1, -1, -1):
            if stack and stack[-1] == '?':
                stack.pop() # ?
                op1 = stack.pop()
                stack.pop # :
                op2 = stack.pop()
                if expression[i] == 'T':
                    stack.append(op1)
                else:
                    stack.append(op2)
            else:
                stack.append(expression[i])
        return stack[0]