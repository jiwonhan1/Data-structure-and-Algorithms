class Solution(object):
    # Time complexity O(T)
    def isSubsequence(self,s,t):
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        def rec_isSubsequence(left_index, right_index):
            if left_index == LEFT_BOUND:
                return True
            if right_index == RIGHT_BOUND:
                return False
            if s[left_index] == s[right_index]:
                left_index += 1
            right_index += 1
            return rec_isSubsequence(left_index, right_index)
        return rec_isSubsequence(0, 0)

    # Time complexity O(T)
    def isSubsequence2(self,s,t):
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)
        left_index = right_index = 0
        while left_index < LEFT_BOUND and right_index < RIGHT_BOUND:
            if s[left_index] == t[right_index]:
                left_index += 1
            right_index += 1
        return left_index == LEFT_BOUND