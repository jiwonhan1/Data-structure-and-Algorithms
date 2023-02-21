class Solution(object):
    def canPermutePalindrome(self,s):
        unpaired_chars = set()

        for c in s:
            if c not in unpaired_chars:
                unpaired_chars.add(c)
            else:
                unpaired_chars.remove(c)
        return len(unpaired_chars) <= 1

# O(N)

    def is_palindrome_permutation(self, phrase):
        table = [0 for _ in range(ord('z') - ord('a') + 1)]
        countodd = 0
        for c in phrase:
            x = self.char_number(c)
            if x != -1:
                table[x] += 1
                if table[x] % 2:
                    countodd += 1
                else:
                    countodd -= 1
        return countodd <= 1

    def char_number(self,c):
        a = ord("a")
        z = ord("z")
        upper_a = ord("A")
        upper_z = ord("Z")
        val = ord(c)

        if a <= val <= z:
            return val - a
        if upper_a <= val <= upper_z:
            return val - upper_a
        return -1
