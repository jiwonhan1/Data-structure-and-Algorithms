class Solution(object):
    # Left-to-Right Pass
    # Each symbol adds its own value, except for when a smaller valued symbol is before a larger valued symbol
    # In those cases, instead of adding both symbols to the total, we need to subtract the large from the small, adding that instead
    # Time complexity O(1) Space complexity O(1)
    # As there is a finite set of roman numerals, the maximum number possible number can be 3999, which in roman numerals is MMMCMXCIX.
    # As such the time complexity is O(1)
    def romanToInt(self, s):
        romanInt = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        i = result = 0

        while i < len(s):
            if i+1 < len(s) and s[i] < s[i+1]:
                result += romanInt[s[i+1]] - romanInt[s[i]]
                i += 2
            else:
                result += romanInt[s[i]]
                i += 1
        return result

