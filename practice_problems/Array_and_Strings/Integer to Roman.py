class Solution(object):
    # Greedy
    # The representation should use the largest possible symbols, working from the left.
    # Therefore, it makes sense to use a Greedy algorithms.
    # A Greedy algorithm is an algorithm that makes the best possible decision at the current time; in this case taking out the largest possible symbol it can.
    # So to represent a given integer, we look for the largest symbol that fits into it.
    # We substract that, and then look for the largest symbol that fits into the reminder, and so on until the reminder is 0.
    # Each of the symbols we take out are appended onto the output Roman Numeral string.
    def intToRoman(self, num):
        digits = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        roman_digits = []

        for value, symbol in digits:
            if num == 0:
                break
            count, num = divmod(num, value)
            roman_digits.append(symbol * count)
        return "".join(roman_digits)