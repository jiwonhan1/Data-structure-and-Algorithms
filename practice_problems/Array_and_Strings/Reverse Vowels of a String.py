class Solution(object):
    def reverseVowels(self, s):
        n_s = len(s)
        keys = {'a', 'e', 'i', 'o', 'u'}
        i,j = 0, n_s-1
        s = list(s)
        while i < j:
            while i < j and s[i] not in keys:
                i += 1
            while i < j and s[j] not in keys:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)



