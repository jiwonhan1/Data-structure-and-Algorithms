class Solution:
    # Time complexity O(n)
    def trim_spaces(self,s):
        left, right = 0, len(s)-1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        output = []
        while left < right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        return output

    def reverse(self, l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
    def reverse_each_words(self, l):
        n = len(l)
        left = right = 0

        while left < n:
            while right < n and l[right] != ' ':
                right += 1
            self.reverse(l, left, right -1)
            left = right + 1
            right += 1
    def reverseWords(self, s):
        l = self.trim_spaces(s)
        self.reverse(l, 0, len(l)-1)
        self.reverse_each_words(l)
        return ''.join(l)