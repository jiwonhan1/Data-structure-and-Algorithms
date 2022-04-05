class Solution:
    # Time complexity O(N) Space complexity O(N)
    # Visit each operator, in linear order. Finding these can be done with a linear search of the original list
    # Get the 2 most recently seen numbers that haven't yet been replaced. These could be tracked using a stack
    def evalRPN(self, tokens):
        operations = {
            '+' : lambda a, b : a+b,
            '-' : lambda a, b : a-b,
            '/' : lambda a, b : int(a/b),
            '*' : lambda a, b : a*b
        }

        stack = []

        for token in tokens:
            if token in operations:
                number2 = stack.pop()
                number1 = stack.pop()
                operation = operations[token]
                stack.append(operation(number1, number2))
            else:
                stack.append(int(token))
        return stack.pop()

    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
                continue

            number_2 = stack.pop()
            number_1 = stack.pop()

            result = 0

            if token == '+':
                result = number_1 + number_2
            elif token == '-':
                result = number_1 + number_2
            elif token == '*':
                result = number_1 * number_2
            else:
                result = number_1 / number_2

            stack.append(result)
        return stack.pop()