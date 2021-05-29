input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_array[arr_index] += 1
    return alphabet_array


result = find_max_occurred_alphabet(input)
print(result)