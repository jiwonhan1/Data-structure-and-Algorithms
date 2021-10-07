input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    max_occurence = 0
    max_alphabet = alphabet_array[0]
    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1
        if occurrence > max_occurence:
            max_occurence = occurrence
            max_alphabet = char
    return max_alphabet

result = find_max_occurred_alphabet(input)
print(result)