# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the 'true' length of the string.

# O(N)

def urlify_algo(string, length):
    # conver to list because PYthon strings are immutable
    char_list = list(string)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == ' ':
            char_list[new_index-3 : new_index] = '%20'
            new_index -= 3
        else:
            char_list[new_index -1] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(char_list[new_index:])

def urlify_pythonic(text, length):
    return text[:length].replace(" ", "%20")


