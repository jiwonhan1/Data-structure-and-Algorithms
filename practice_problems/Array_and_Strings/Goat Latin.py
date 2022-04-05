class Solution:
    def toGoatLatin(self, sentence):
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = []

        for i,w in enumerate(sentence.split()):
            if w[0].lower in vowels:
                temp = w + 'ma' + 'a' * (i+1)
                res.append(temp)
            else:
                temp = w[1:] + w[0] + 'ma' + 'a' * (i+1)
                res.append(temp)
        return ' '.join(res)