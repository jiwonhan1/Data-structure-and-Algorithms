class Solution(object):
    def reverseWords(self,s):
        temp = s.split()
        result = ""
        for word in temp:
            word = word[::-1]
            result += word + ' '
        return result[:-1]
