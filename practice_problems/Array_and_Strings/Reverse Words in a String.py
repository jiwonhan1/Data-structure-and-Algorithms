from collections import deque
class Solution:
    # built in split and reverse
    # Time complexity O(N) Space complexity O(N)
    def reverseWords(self, s):
        return ''.join(reversed(s.split()))

    # Reverse the Whole string and then reverse each word
    # Time complexity O(n) Space complexity O(N)
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

    # Deque of Words
    # Time and space complexity O(N)
    def reverseWords(self, s):
        left, right = 0, len(s) -1
        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1

        d, word = deque(), []
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))
        return ' '.join(d)
