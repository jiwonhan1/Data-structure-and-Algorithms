from collections import deque

balanced_parentheses_string = "()))((()"

def is_correct_parenthesis(balanced_parentheses_string):
    stack = []
    for s in balanced_parentheses_string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def change_to_correct_parenthesis(string):
    if string == '':
        return ''
    u, v = separate_to_u_v(string)
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
    else:
        return '(' + change_to_correct_parenthesis(v) + ')' + reverse_parentheses(u[1:-1])

def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = ''.join(list(queue))
    return u, v

def reverse_parentheses(string):
    reversed_string = ""
    for char in string:
        if char == "(":
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string



def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)

print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!