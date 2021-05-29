input = "abaabadce"


def find_not_repeating_character(string):
    alphabet_occurance_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurance_array[arr_index] += 1
    not_repeating_character_array = []
    for index, alphabet in enumerate(alphabet_occurance_array):
        if alphabet == 1:
            not_repeating_character_array.append(chr(index + ord("a")))
    for char in string:
        if char in not_repeating_character_array:
            return char

result = find_not_repeating_character(input)
print(result)