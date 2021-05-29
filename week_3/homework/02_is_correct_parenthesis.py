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


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!