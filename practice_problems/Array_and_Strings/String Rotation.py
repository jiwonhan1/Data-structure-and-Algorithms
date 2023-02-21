class Solution:

    # O(N)
    def string_rotation(self, s1, s2):
        if len(s1) == len(s2) != 0:
            return s2 in s1 * 2

        return False