# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique_chars_algorithm(string):
    # Assuming character set is ASCII (128 character)
    if len(string) > 128:
        return False
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True

def is_unique_chars_pythonic(string):
    return len(set(string)) == len(string)

def is_unique_chars_using_dictionary(string):
    character_count = {}
    for char in string:
        if char in character_count:
            return False
        character_count[char] = 1
    return True

def is_unique_chars_using_set(string):
    characters_seen = set()
    for char in string:
        if char in characters_seen:
            return False
        characters_seen.add(char)
    return True

# O(NlogN)
def is_unique_chars_sorting(string):
    sorted_string = sorted(string)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True
