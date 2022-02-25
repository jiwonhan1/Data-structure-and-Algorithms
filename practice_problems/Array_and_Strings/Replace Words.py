class Solution(object):
    # Prefix Hash
    def replaceWords(self, dictionary, sentence):
        rootset = set(dictionary)
        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word
        return ' '.join(map(replace, sentence.split()))