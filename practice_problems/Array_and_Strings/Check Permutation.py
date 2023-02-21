# O(N)
# Given two strings, write a method to decide if one is a permutation of the other

from collections import Counter

def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def check_permutation_by_count(s1, s2):
    if len(s1) != len(s2):
        return False
    counter = [0] * 256
    for c in s1:
        counter[ord(c)] += 1
    for c in s2:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1
    return True

