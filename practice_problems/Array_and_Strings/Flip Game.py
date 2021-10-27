class Solution(object):
    def generatePossibleNextMoves(self,s):
        ret = []
        for i in range(len(s) -1):
            if s[i:i+2] == "++":
                flip = s[:i] + "--" + s[i+2:]
                ret.append(flip)
        return ret

    def generatePossibleNextMoves2(self,s):
        return [s[:i] + "--" + s[i+2:] for i in range(len(s)-1) if s[i:i+2] == "++"]