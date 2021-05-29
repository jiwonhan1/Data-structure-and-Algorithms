input = "tomato"


def is_palindrome(string):
    middle = len(string) // 2
    length = len(string) -1
    count = 0
    str = ""
    while middle > count:
        str += string[length]
        length -= 1
        count += 1
    print(str)
    print(string[0:middle])
    if str == string[0:middle]:
        return True
    return False


print(is_palindrome(input))