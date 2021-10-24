class Solution:
    def validWordSquare(self, words):
        row, col = len(words), len(words[0])
        i = j = 0

        for i in range(row):
            temp = ''
            for j in range(col):
                if i < len(words[j]):
                    temp += words[j][i]
                else:
                    break
            if temp != words[i]:
                return False
        return True
