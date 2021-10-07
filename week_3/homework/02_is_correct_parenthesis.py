s = "(())())"


def is_correct_parenthesis(string):
    strArray = list(string)
    strArray.sort()
    i = 0
    while i < len(strArray):
        if strArray[i] == "(" and strArray[-1] == ")":
            strArray.pop()
        i += 1
    print(strArray)
    if ")" in strArray: return False
    return True

def is_correct_parenthesis2(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!